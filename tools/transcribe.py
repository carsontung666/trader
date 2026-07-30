#!/usr/bin/env python3
"""Transcribe the course videos with timestamps using faster-whisper."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from faster_whisper import WhisperModel


COURSE_DIR = Path("/home/junyao/25 9月最新PRO+专属进阶课")
OUTPUT_DIR = COURSE_DIR / "学习资料" / "01_转写稿"
INITIAL_PROMPT = (
    "这是一门美股日内交易 Day Trading 进阶课，中文讲解中夹杂英文交易术语。"
    "请准确识别：阻力位 resistance、支撑位 support、趋势 trend、Level 2、"
    "bid、ask、spread、position size、profit、risk、stop loss、做空 short、"
    "借股 locate/borrow、Hotkey、order、market order、limit order、"
    "stop order、DAS Trader、Trade Ideas、股票同步、ticker、INVO。"
)


def stamp(seconds: float, srt: bool = False) -> str:
    milliseconds = max(0, round(seconds * 1000))
    hours, milliseconds = divmod(milliseconds, 3_600_000)
    minutes, milliseconds = divmod(milliseconds, 60_000)
    secs, milliseconds = divmod(milliseconds, 1000)
    separator = "," if srt else "."
    return f"{hours:02d}:{minutes:02d}:{secs:02d}{separator}{milliseconds:03d}"


def transcribe_one(model: WhisperModel, video: Path, overwrite: bool) -> None:
    stem = video.stem
    json_path = OUTPUT_DIR / f"{stem}.json"
    md_path = OUTPUT_DIR / f"{stem}.md"
    srt_path = OUTPUT_DIR / f"{stem}.srt"
    if json_path.exists() and md_path.exists() and srt_path.exists() and not overwrite:
        print(f"SKIP {video.name}", flush=True)
        return

    print(f"START {video.name}", flush=True)
    segments_iter, info = model.transcribe(
        str(video),
        language="zh",
        task="transcribe",
        beam_size=5,
        best_of=5,
        temperature=0,
        vad_filter=True,
        vad_parameters={
            "min_silence_duration_ms": 500,
            "speech_pad_ms": 250,
        },
        word_timestamps=True,
        condition_on_previous_text=False,
        repetition_penalty=1.08,
        no_repeat_ngram_size=4,
        hallucination_silence_threshold=2,
        initial_prompt=INITIAL_PROMPT,
    )

    segments = []
    for index, segment in enumerate(segments_iter, 1):
        words = [
            {
                "start": word.start,
                "end": word.end,
                "word": word.word,
                "probability": word.probability,
            }
            for word in (segment.words or [])
        ]
        item = {
            "id": segment.id,
            "start": segment.start,
            "end": segment.end,
            "text": segment.text.strip(),
            "avg_logprob": segment.avg_logprob,
            "no_speech_prob": segment.no_speech_prob,
            "words": words,
        }
        segments.append(item)
        print(
            f"  {index:04d} [{stamp(segment.start)} --> {stamp(segment.end)}] "
            f"{segment.text.strip()}",
            flush=True,
        )

    payload = {
        "source": str(video),
        "model": "Systran/faster-whisper-large-v3",
        "detected_language": info.language,
        "language_probability": info.language_probability,
        "duration_seconds": info.duration,
        "duration_after_vad_seconds": info.duration_after_vad,
        "segments": segments,
    }
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    md_lines = [
        f"# {stem}：带时间戳转写",
        "",
        f"- 视频：`{video.name}`",
        f"- 时长：{stamp(info.duration)}",
        f"- 识别语言：{info.language}（置信度 {info.language_probability:.3f}）",
        "- 说明：这是自动转写底稿，讲义会结合视频画面校正术语与上下文。",
        "",
    ]
    for segment in segments:
        md_lines.append(
            f"**[{stamp(segment['start'])}–{stamp(segment['end'])}]** "
            f"{segment['text']}"
        )
        md_lines.append("")
    md_path.write_text("\n".join(md_lines), encoding="utf-8")

    srt_lines = []
    for index, segment in enumerate(segments, 1):
        srt_lines.extend(
            [
                str(index),
                f"{stamp(segment['start'], srt=True)} --> {stamp(segment['end'], srt=True)}",
                segment["text"],
                "",
            ]
        )
    srt_path.write_text("\n".join(srt_lines), encoding="utf-8")
    print(f"DONE {video.name}: {len(segments)} segments", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "videos",
        nargs="*",
        help="Video filenames or numeric prefixes (default: all MP4 files).",
    )
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    all_videos = sorted(COURSE_DIR.glob("*.mp4"))
    if args.videos:
        requested = set(args.videos)
        videos = [
            video
            for video in all_videos
            if video.name in requested
            or video.stem in requested
            or video.name.split(".", 1)[0] in requested
        ]
        if not videos:
            raise SystemExit(f"No videos matched: {', '.join(args.videos)}")
    else:
        videos = all_videos

    model = WhisperModel(
        "Systran/faster-whisper-large-v3",
        device="cuda",
        compute_type="float16",
        download_root="/home/junyao/.cache/huggingface",
    )
    for video in videos:
        transcribe_one(model, video, args.overwrite)


if __name__ == "__main__":
    main()
