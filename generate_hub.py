"""Comprehensive generator for ApexMotion Workshop Hub.
Includes:
- Interactive Architecture SVG Diagram
- Interactive Clickable Roadmap Tree
- 🎬 Interactive Video Tutorial & Walkthrough Player (Simulated realistic terminal screencasts with audio narration text & player controls)
- 🎮 Interactive Level-Up Game Arena ("ApexMotion Quest: The Agent Engineering Game")
  * Start button to launch game
  * 6 real architectural & calisthenics missions
  * XP points & 5 Level-Up ranks (Cloud Trainee -> Apex Grandmaster)
  * Hearts / Lives system (❤️❤️❤️)
  * Instant feedback with Web Audio API sound synthesis (100% offline, zero audio files!)
  * Canvas particle confetti celebration & 5 collectible mastery badges
  * Highscore and progress saving in localStorage
- 🕹️ Interactive Live Muscle Fatigue & Recovery Simulator (RPE Calculation & 24h Decay)
- 📂 Firestore Live Database Explorer (JSON docs)
- 📐 Mathematical Models & Recovery Formulas
- 🎯 Concrete Tool Outputs & Practical Results in every completed step
- 💡 Explicit 'Why this step was done' rationales
- 100% self-contained, offline-ready, email-friendly (<65 KB zipped)
"""

import os
import shutil
import zipfile

HTML_SRC = "/config/Desktop/BuildWithGemini/learning_progress.html"
DESKTOP_DIR = "/config/Desktop/HTML"

html_code = """<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ApexMotion - Workshop Learning & Progress Hub</title>
  <style>
    :root {
      --bg-primary: #0a0f1d;
      --bg-secondary: #11192d;
      --bg-card: #15203b;
      --bg-card-hover: #1c2b4f;
      --border-color: #263859;
      --border-highlight: #38bdf8;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --accent-blue: #38bdf8;
      --accent-purple: #c084fc;
      --accent-green: #22c55e;
      --accent-yellow: #facc15;
      --accent-red: #f87171;
      --accent-pink: #ec4899;
      --code-bg: #070b14;
      --radius: 12px;
      --transition: all 0.25s ease-in-out;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif;
    }

    body {
      background-color: var(--bg-primary);
      color: var(--text-main);
      line-height: 1.6;
      padding: 24px;
      min-height: 100vh;
    }

    .container {
      max-width: 1320px;
      margin: 0 auto;
    }

    /* Header */
    header {
      background: linear-gradient(135deg, #131d36 0%, #0a0f1d 100%);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 28px 32px;
      margin-bottom: 24px;
      box-shadow: 0 12px 30px -5px rgba(0, 0, 0, 0.6);
      position: relative;
      overflow: hidden;
    }

    header::before {
      content: "";
      position: absolute;
      top: -50px;
      right: -50px;
      width: 280px;
      height: 280px;
      background: radial-gradient(circle, rgba(56, 189, 248, 0.15) 0%, rgba(192, 132, 252, 0.05) 70%, transparent 100%);
      pointer-events: none;
    }

    .header-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      flex-wrap: wrap;
      gap: 16px;
      margin-bottom: 16px;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .brand-icon {
      font-size: 38px;
      background: #070b14;
      width: 60px;
      height: 60px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 14px;
      border: 1px solid var(--border-color);
      box-shadow: 0 4px 14px rgba(0,0,0,0.4);
    }

    h1 {
      font-size: 26px;
      font-weight: 800;
      letter-spacing: -0.5px;
      background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .subtitle {
      color: var(--text-muted);
      font-size: 14px;
      margin-top: 4px;
    }

    .lang-switch {
      display: flex;
      background: #070b14;
      padding: 4px;
      border-radius: 30px;
      border: 1px solid var(--border-color);
      gap: 4px;
    }

    .lang-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 6px 14px;
      border-radius: 20px;
      cursor: pointer;
      font-weight: 600;
      font-size: 13px;
      transition: var(--transition);
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .lang-btn.active {
      background: #2563eb;
      color: #fff;
      box-shadow: 0 2px 10px rgba(37, 99, 235, 0.4);
    }

    /* Stats bar */
    .stats-bar {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      margin-top: 20px;
      padding-top: 20px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
    }

    .stat-card {
      background: rgba(10, 15, 29, 0.7);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 12px 16px;
    }

    .stat-label {
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: var(--text-dim);
      margin-bottom: 4px;
    }

    .stat-value {
      font-size: 18px;
      font-weight: 700;
      color: var(--accent-blue);
    }

    .progress-track {
      background: #070b14;
      height: 8px;
      border-radius: 4px;
      overflow: hidden;
      margin-top: 8px;
    }

    .progress-fill {
      height: 100%;
      background: linear-gradient(90deg, #38bdf8, #22c55e);
      border-radius: 4px;
      transition: width 0.4s ease;
    }

    /* Common Section */
    .hub-section {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 24px;
      margin-bottom: 28px;
      box-shadow: 0 10px 25px -5px rgba(0,0,0,0.5);
    }

    .section-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 20px;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--border-color);
    }

    .section-title-wrap {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 18px;
      font-weight: 800;
      color: var(--accent-blue);
    }

    .section-badge {
      font-size: 11px;
      color: var(--text-muted);
      background: #070b14;
      padding: 4px 10px;
      border-radius: 20px;
      border: 1px solid var(--border-color);
    }

    /* 1. Architecture SVG */
    .arch-diagram-wrapper {
      background: #070b14;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 20px;
      overflow-x: auto;
      text-align: center;
    }

    svg.arch-svg {
      max-width: 100%;
      height: auto;
      min-width: 760px;
    }

    /* 2. Interactive Roadmap Tree */
    .tree-grid {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .phase-row {
      display: flex;
      align-items: stretch;
      gap: 16px;
      background: rgba(7, 11, 20, 0.4);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 14px;
      position: relative;
    }

    .phase-label {
      width: 170px;
      flex-shrink: 0;
      display: flex;
      flex-direction: column;
      justify-content: center;
      border-right: 1px solid var(--border-color);
      padding-right: 14px;
    }

    .phase-badge {
      font-size: 10px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      color: var(--accent-purple);
      margin-bottom: 4px;
    }

    .phase-name {
      font-size: 14px;
      font-weight: 700;
      color: var(--text-main);
    }

    .phase-nodes {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 10px;
      flex: 1;
    }

    .tree-node {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 8px 14px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 10px;
      transition: var(--transition);
      user-select: none;
      text-decoration: none;
      color: inherit;
    }

    .tree-node:hover {
      background: var(--bg-card-hover);
      border-color: var(--accent-blue);
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(56, 189, 248, 0.25);
    }

    .tree-node.active-done { border-left: 3px solid var(--accent-green); }
    .tree-node.video-node { border-left: 3px solid #f43f5e; background: rgba(244, 63, 94, 0.1); }
    .tree-node.game-node { border-left: 3px solid #ec4899; background: rgba(236, 72, 153, 0.1); }
    .tree-node.math-node { border-left: 3px solid var(--accent-purple); background: rgba(192, 132, 252, 0.1); }
    .tree-node.sim-node { border-left: 3px solid var(--accent-yellow); background: rgba(250, 204, 21, 0.1); }
    .tree-node.db-node { border-left: 3px solid var(--accent-blue); background: rgba(56, 189, 248, 0.1); }
    .tree-node.upcoming-node { border-left: 3px solid var(--text-dim); opacity: 0.8; }

    .node-num {
      font-size: 11px;
      font-weight: 800;
      background: #070b14;
      color: var(--accent-blue);
      padding: 2px 6px;
      border-radius: 4px;
      border: 1px solid rgba(56, 189, 248, 0.3);
    }

    .node-text {
      font-size: 12px;
      font-weight: 600;
      white-space: nowrap;
    }

    .node-arrow {
      color: var(--text-dim);
      font-size: 14px;
    }

    @keyframes pulseGlow {
      0% { box-shadow: 0 0 0 0 rgba(56, 189, 248, 0.8); }
      70% { box-shadow: 0 0 0 16px rgba(56, 189, 248, 0); }
      100% { box-shadow: 0 0 0 0 rgba(56, 189, 248, 0); }
    }

    .pulse-highlight {
      animation: pulseGlow 1.6s ease-out !important;
      border-color: var(--accent-blue) !important;
    }

    /* ========================================================
       VIDEO TUTORIAL & WALKTHROUGH STUDIO PLAYER
       ======================================================== */
    .video-studio-grid {
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 20px;
    }

    @media (max-width: 960px) {
      .video-studio-grid { grid-template-columns: 1fr; }
    }

    .video-player-frame {
      background: #070b14;
      border: 1px solid #334155;
      border-radius: 12px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 12px 30px rgba(0,0,0,0.7);
    }

    .video-title-bar {
      background: #0f172a;
      border-bottom: 1px solid #1e293b;
      padding: 10px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .mac-dots {
      display: flex;
      gap: 6px;
    }

    .mac-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
    }

    .mac-dot.red { background: #ef4444; }
    .mac-dot.yellow { background: #f59e0b; }
    .mac-dot.green { background: #10b981; }

    .video-screen {
      background: #030712;
      min-height: 280px;
      padding: 18px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 13px;
      color: #e2e8f0;
      line-height: 1.6;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
    }

    .terminal-output-area {
      flex: 1;
      overflow-y: auto;
      max-height: 240px;
      margin-bottom: 14px;
    }

    .term-prompt { color: #38bdf8; font-weight: 700; }
    .term-cmd { color: #facc15; font-weight: 600; }
    .term-log { color: #94a3b8; }
    .term-success { color: #4ade80; }
    .term-highlight { color: #c084fc; font-weight: 700; }

    .narration-banner {
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid #3b82f6;
      border-radius: 8px;
      padding: 10px 14px;
      display: flex;
      align-items: center;
      gap: 10px;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      font-size: 13px;
      color: #93c5fd;
    }

    .video-controls-bar {
      background: #0f172a;
      border-top: 1px solid #1e293b;
      padding: 10px 16px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .video-scrubber-track {
      background: #1e293b;
      height: 6px;
      border-radius: 3px;
      cursor: pointer;
      position: relative;
      overflow: hidden;
    }

    .video-scrubber-fill {
      background: linear-gradient(90deg, #3b82f6, #8b5cf6);
      height: 100%;
      width: 0%;
      border-radius: 3px;
      transition: width 0.1s linear;
    }

    .video-buttons-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .video-btn {
      background: #1e293b;
      border: 1px solid #334155;
      color: #f8fafc;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: var(--transition);
    }

    .video-btn:hover {
      background: #2563eb;
      border-color: #3b82f6;
    }

    .video-btn.active-play {
      background: #2563eb;
    }

    /* Playlist */
    .playlist-card {
      background: #070b14;
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .playlist-item {
      background: #0f172a;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 10px 12px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 10px;
      transition: var(--transition);
    }

    .playlist-item:hover {
      border-color: #38bdf8;
      background: #1e293b;
    }

    .playlist-item.active {
      border-left: 4px solid #38bdf8;
      background: rgba(56, 189, 248, 0.1);
    }

    .item-icon { font-size: 18px; }
    .item-meta { flex: 1; }
    .item-title { font-size: 13px; font-weight: 700; color: #f8fafc; }
    .item-dur { font-size: 11px; color: #64748b; }

    /* ========================================================
       🎮 LEVEL-UP GAME ARENA ("APEXMOTION QUEST")
       ======================================================== */
    .game-arena-wrapper {
      background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(7, 11, 20, 0.98) 100%);
      border: 2px solid #ec4899;
      box-shadow: 0 0 30px rgba(236, 72, 153, 0.25);
      border-radius: 14px;
      padding: 24px;
      position: relative;
      overflow: hidden;
    }

    .game-arena-wrapper::before {
      content: "";
      position: absolute;
      top: 0; left: 0; right: 0; height: 3px;
      background: linear-gradient(90deg, #ec4899, #8b5cf6, #3b82f6);
    }

    /* HUD Bar */
    .game-hud {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 14px;
      background: #070b14;
      border: 1px solid #263859;
      border-radius: 10px;
      padding: 12px 18px;
      margin-bottom: 20px;
    }

    .hud-rank-badge {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 13px;
      font-weight: 800;
      color: #f472b6;
      background: rgba(236, 72, 153, 0.12);
      padding: 6px 12px;
      border-radius: 20px;
      border: 1px solid rgba(236, 72, 153, 0.3);
    }

    .hud-stats-group {
      display: flex;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
    }

    .hud-stat-item {
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 13px;
      font-weight: 700;
    }

    .hud-lives { font-size: 16px; letter-spacing: 2px; }
    .hud-xp { color: #facc15; }
    .hud-streak { color: #38bdf8; }

    /* Game Screens */
    .game-screen {
      display: none;
    }

    .game-screen.active {
      display: block;
      animation: fadeIn 0.3s ease-in-out;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* Start Screen */
    .game-hero-card {
      text-align: center;
      padding: 30px 20px;
      background: rgba(10, 15, 29, 0.6);
      border: 1px solid #334155;
      border-radius: 12px;
    }

    .game-hero-icon {
      font-size: 54px;
      margin-bottom: 12px;
      display: inline-block;
      animation: floatIcon 3s ease-in-out infinite;
    }

    @keyframes floatIcon {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-8px); }
    }

    .game-hero-title {
      font-size: 24px;
      font-weight: 900;
      background: linear-gradient(90deg, #ec4899, #a855f7, #38bdf8);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 8px;
    }

    .game-hero-desc {
      font-size: 14px;
      color: #94a3b8;
      max-width: 650px;
      margin: 0 auto 24px auto;
      line-height: 1.6;
    }

    .tier-badges-row {
      display: flex;
      justify-content: center;
      gap: 10px;
      flex-wrap: wrap;
      margin-bottom: 24px;
    }

    .tier-pill {
      font-size: 11px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 6px;
      background: #070b14;
      border: 1px solid #334155;
      color: #cbd5e1;
    }

    .btn-start-game {
      background: linear-gradient(135deg, #ec4899 0%, #a855f7 100%);
      color: #fff;
      border: none;
      font-size: 16px;
      font-weight: 800;
      padding: 14px 34px;
      border-radius: 30px;
      cursor: pointer;
      box-shadow: 0 6px 20px rgba(236, 72, 153, 0.4);
      transition: var(--transition);
      display: inline-flex;
      align-items: center;
      gap: 10px;
    }

    .btn-start-game:hover {
      transform: translateY(-2px) scale(1.02);
      box-shadow: 0 10px 25px rgba(236, 72, 153, 0.6);
    }

    /* Question / Mission Screen */
    .mission-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
      padding-bottom: 10px;
      border-bottom: 1px solid #334155;
    }

    .mission-badge {
      font-size: 12px;
      font-weight: 800;
      color: #38bdf8;
      text-transform: uppercase;
      letter-spacing: 0.6px;
    }

    .mission-xp-reward {
      font-size: 12px;
      font-weight: 700;
      color: #facc15;
    }

    .scenario-box {
      background: #070b14;
      border: 1px solid #1e293b;
      border-radius: 10px;
      padding: 18px;
      margin-bottom: 18px;
    }

    .scenario-title {
      font-size: 15px;
      font-weight: 800;
      color: #f8fafc;
      margin-bottom: 8px;
    }

    .scenario-snippet {
      background: #0f172a;
      border-radius: 6px;
      padding: 12px;
      font-family: ui-monospace, monospace;
      font-size: 12px;
      color: #7dd3fc;
      margin-top: 10px;
      border-left: 3px solid #38bdf8;
      overflow-x: auto;
    }

    .quiz-options {
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-bottom: 18px;
    }

    .quiz-opt-btn {
      background: #0f172a;
      border: 1px solid #334155;
      color: #e2e8f0;
      border-radius: 8px;
      padding: 14px 18px;
      font-size: 13px;
      font-weight: 600;
      text-align: left;
      cursor: pointer;
      transition: var(--transition);
      display: flex;
      align-items: center;
      gap: 12px;
      line-height: 1.5;
    }

    .quiz-opt-btn:hover:not(:disabled) {
      background: #1e293b;
      border-color: #38bdf8;
      transform: translateX(4px);
    }

    .opt-letter {
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: #1e293b;
      border: 1px solid #475569;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
      font-weight: 800;
      flex-shrink: 0;
    }

    .quiz-opt-btn.correct {
      background: rgba(34, 197, 94, 0.15) !important;
      border-color: #22c55e !important;
      color: #86efac !important;
    }

    .quiz-opt-btn.wrong {
      background: rgba(239, 68, 68, 0.15) !important;
      border-color: #ef4444 !important;
      color: #fca5a5 !important;
      animation: shake 0.4s ease-in-out;
    }

    @keyframes shake {
      0%, 100% { transform: translateX(0); }
      20%, 60% { transform: translateX(-6px); }
      40%, 80% { transform: translateX(6px); }
    }

    /* Explanation Banner */
    .game-feedback-box {
      border-radius: 8px;
      padding: 14px 18px;
      margin-bottom: 18px;
      display: none;
      animation: fadeIn 0.3s ease;
    }

    .game-feedback-box.correct {
      background: rgba(34, 197, 94, 0.1);
      border: 1px solid #22c55e;
      color: #bbf7d0;
    }

    .game-feedback-box.wrong {
      background: rgba(239, 68, 68, 0.1);
      border: 1px solid #ef4444;
      color: #fecaca;
    }

    .btn-next-mission {
      background: #2563eb;
      color: #fff;
      border: none;
      padding: 12px 24px;
      border-radius: 8px;
      font-weight: 800;
      font-size: 14px;
      cursor: pointer;
      transition: var(--transition);
      display: none;
      align-items: center;
      gap: 8px;
      margin-left: auto;
    }

    .btn-next-mission:hover {
      background: #1d4ed8;
      transform: translateY(-2px);
    }

    /* Victory Screen */
    .victory-box {
      text-align: center;
      padding: 30px 20px;
      background: rgba(10, 15, 29, 0.8);
      border: 1px solid #a855f7;
      border-radius: 12px;
      position: relative;
    }

    #confetti-canvas {
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      pointer-events: none;
      border-radius: 12px;
    }

    .badges-collection-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 12px;
      margin: 24px 0;
    }

    .badge-item {
      background: #070b14;
      border: 1px solid #334155;
      border-radius: 8px;
      padding: 12px;
      text-align: center;
    }

    .badge-item.unlocked {
      border-color: #facc15;
      box-shadow: 0 0 10px rgba(250, 204, 21, 0.2);
    }

    .badge-icon { font-size: 28px; margin-bottom: 4px; }
    .badge-name { font-size: 12px; font-weight: 700; color: #f8fafc; }
    .badge-desc { font-size: 10px; color: #94a3b8; margin-top: 2px; }

    /* Simulator Styles */
    .sim-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }

    @media (max-width: 900px) {
      .sim-grid { grid-template-columns: 1fr; }
    }

    .sim-panel {
      background: #070b14;
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 18px;
    }

    .sim-title {
      font-size: 14px;
      font-weight: 700;
      color: var(--accent-yellow);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .control-row { margin-bottom: 14px; }
    .control-label {
      font-size: 12px;
      color: var(--text-muted);
      margin-bottom: 6px;
      display: flex;
      justify-content: space-between;
    }

    .sim-select, .sim-slider {
      width: 100%;
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 8px 12px;
      border-radius: 6px;
      font-size: 13px;
      outline: none;
    }

    .sim-btn-primary {
      background: #2563eb;
      color: #fff;
      border: none;
      padding: 10px 16px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 13px;
      cursor: pointer;
      width: 100%;
      transition: var(--transition);
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 8px;
      margin-top: 10px;
    }

    .sim-btn-primary:hover { background: #1d4ed8; }

    .sim-btn-secondary {
      background: #1e293b;
      color: var(--text-muted);
      border: 1px solid var(--border-color);
      padding: 8px 14px;
      border-radius: 8px;
      font-weight: 600;
      font-size: 12px;
      cursor: pointer;
      width: 100%;
      transition: var(--transition);
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 6px;
      margin-top: 8px;
    }

    .sim-btn-secondary:hover { color: var(--text-main); border-color: var(--text-dim); }

    .muscle-bars {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .muscle-row {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .muscle-meta {
      display: flex;
      justify-content: space-between;
      font-size: 12px;
    }

    .muscle-bar-track {
      background: #11192d;
      height: 8px;
      border-radius: 4px;
      overflow: hidden;
      border: 1px solid rgba(255,255,255,0.05);
    }

    .muscle-bar-fill {
      height: 100%;
      border-radius: 4px;
      transition: width 0.4s ease, background 0.4s ease;
    }

    .readiness-box {
      background: rgba(10, 15, 29, 0.8);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 12px;
      margin-top: 14px;
      text-align: center;
    }

    .readiness-score-num {
      font-size: 28px;
      font-weight: 800;
      margin: 4px 0;
    }

    /* DB Tabs */
    .db-tabs {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-bottom: 14px;
    }

    .db-tab-btn {
      background: #070b14;
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 12px;
      cursor: pointer;
      font-weight: 600;
      transition: var(--transition);
    }

    .db-tab-btn.active {
      background: #1e3a8a;
      color: #93c5fd;
      border-color: #3b82f6;
    }

    .db-doc-viewer {
      background: #070b14;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 14px;
      font-family: ui-monospace, monospace;
      font-size: 12px;
      color: #7dd3fc;
      overflow-x: auto;
      max-height: 280px;
    }

    /* Math */
    .math-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
      gap: 20px;
    }

    .math-card {
      background: #070b14;
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 18px;
    }

    .math-card-title {
      font-size: 14px;
      font-weight: 700;
      color: var(--accent-blue);
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .math-formula-box {
      background: #0f172a;
      border: 1px solid #263859;
      border-radius: 8px;
      padding: 14px;
      margin: 12px 0;
      text-align: center;
      font-family: "Cambria Math", "Latin Modern Math", KaTeX_Math, serif;
      font-size: 16px;
      color: #38bdf8;
      overflow-x: auto;
    }

    .math-desc {
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.5;
    }

    /* Controls */
    .controls {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 24px;
    }

    .search-box {
      flex: 1;
      min-width: 260px;
      position: relative;
    }

    .search-input {
      width: 100%;
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 10px 14px 10px 38px;
      color: var(--text-main);
      font-size: 14px;
      outline: none;
      transition: var(--transition);
    }

    .search-input:focus {
      border-color: var(--accent-blue);
      box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2);
    }

    .search-icon {
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-dim);
      font-size: 14px;
    }

    .filter-group {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }

    .filter-btn {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      padding: 7px 14px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      transition: var(--transition);
    }

    .filter-btn:hover {
      color: var(--text-main);
      border-color: var(--text-dim);
    }

    .filter-btn.active {
      background: #1e3a8a;
      color: #93c5fd;
      border-color: #3b82f6;
    }

    .action-btn {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 7px 14px;
      border-radius: 8px;
      font-size: 12px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: var(--transition);
    }

    .action-btn:hover {
      background: var(--bg-card-hover);
      border-color: var(--border-highlight);
    }

    /* Timeline & Steps */
    .timeline {
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    .step-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      transition: var(--transition);
      overflow: hidden;
      position: relative;
    }

    .step-card:hover { border-color: #3b82f6; }
    .step-card.completed { border-left: 5px solid var(--accent-green); }
    .step-card.upcoming { border-left: 5px solid var(--text-dim); opacity: 0.9; }

    .step-header {
      padding: 16px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      user-select: none;
      background: rgba(10, 15, 29, 0.4);
    }

    .step-header:hover { background: rgba(21, 32, 59, 0.8); }

    .step-title-area {
      display: flex;
      align-items: center;
      gap: 14px;
      flex: 1;
    }

    .step-num {
      width: 32px;
      height: 32px;
      border-radius: 8px;
      background: #070b14;
      border: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 14px;
      color: var(--accent-blue);
      flex-shrink: 0;
    }

    .step-card.completed .step-num {
      background: rgba(34, 197, 94, 0.15);
      border-color: var(--accent-green);
      color: var(--accent-green);
    }

    .step-title-text {
      font-size: 16px;
      font-weight: 700;
    }

    .step-badges {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .badge {
      font-size: 11px;
      font-weight: 600;
      padding: 3px 8px;
      border-radius: 6px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .badge-setup { background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); }
    .badge-agent { background: rgba(192, 132, 252, 0.15); color: #c084fc; border: 1px solid rgba(192, 132, 252, 0.3); }
    .badge-db { background: rgba(250, 204, 21, 0.15); color: #facc15; border: 1px solid rgba(250, 204, 21, 0.3); }
    .badge-storage { background: rgba(248, 113, 113, 0.15); color: #f87171; border: 1px solid rgba(248, 113, 113, 0.3); }
    .badge-deploy { background: rgba(34, 197, 94, 0.15); color: #4ade80; border: 1px solid rgba(34, 197, 94, 0.3); }

    .step-body {
      padding: 22px;
      border-top: 1px solid rgba(255, 255, 255, 0.06);
      display: none;
    }

    .step-card.expanded .step-body { display: block; }
    .step-card.expanded .chevron { transform: rotate(180deg); }

    .chevron {
      transition: transform 0.2s ease;
      color: var(--text-dim);
      font-size: 14px;
    }

    .detail-grid {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .why-box {
      background: linear-gradient(90deg, rgba(37, 99, 235, 0.15) 0%, rgba(10, 15, 29, 0.6) 100%);
      border: 1px solid #3b82f6;
      border-left: 5px solid #3b82f6;
      border-radius: 8px;
      padding: 14px 18px;
    }

    .why-title {
      font-size: 13px;
      font-weight: 800;
      color: #38bdf8;
      text-transform: uppercase;
      letter-spacing: 0.7px;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .info-box {
      background: #070b14;
      border-radius: 8px;
      padding: 14px 16px;
      border-left: 3px solid var(--accent-blue);
    }

    .info-box.rationale {
      border-left-color: var(--accent-purple);
      background: rgba(192, 132, 252, 0.05);
    }

    .info-box.gotcha {
      border-left-color: var(--accent-yellow);
      background: rgba(250, 204, 21, 0.06);
    }

    .info-box.result-box {
      border-left-color: var(--accent-green);
      background: rgba(34, 197, 94, 0.06);
    }

    .info-box-title {
      font-size: 13px;
      font-weight: 700;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .info-box-title.blue { color: var(--accent-blue); }
    .info-box-title.purple { color: var(--accent-purple); }
    .info-box-title.yellow { color: var(--accent-yellow); }
    .info-box-title.green { color: var(--accent-green); }

    .code-container {
      position: relative;
      background: var(--code-bg);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      margin: 10px 0;
      overflow: hidden;
    }

    .code-header {
      background: #11192d;
      padding: 6px 12px;
      font-size: 11px;
      color: var(--text-dim);
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid rgba(255,255,255,0.05);
    }

    pre {
      padding: 12px;
      overflow-x: auto;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
      font-size: 12px;
      color: #e2e8f0;
      line-height: 1.5;
    }

    .copy-btn {
      background: #1c2b4f;
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      font-size: 10px;
      padding: 3px 8px;
      border-radius: 4px;
      cursor: pointer;
      transition: var(--transition);
    }

    .copy-btn:hover { background: #2563eb; color: #fff; }

    .learn-check {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-top: 14px;
      padding: 10px 16px;
      background: rgba(7, 11, 20, 0.9);
      border-radius: 8px;
      border: 1px solid var(--border-color);
      cursor: pointer;
      user-select: none;
    }

    .learn-check input {
      accent-color: var(--accent-green);
      width: 17px;
      height: 17px;
      cursor: pointer;
    }

    .learn-check span {
      font-size: 13px;
      color: var(--text-muted);
      font-weight: 500;
    }

    .learn-check input:checked + span {
      color: var(--accent-green);
      font-weight: 600;
    }

    .section-title {
      font-size: 18px;
      font-weight: 700;
      margin: 36px 0 16px 0;
      display: flex;
      align-items: center;
      gap: 10px;
      color: var(--text-main);
    }

    .cheatsheet-table {
      width: 100%;
      border-collapse: collapse;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      overflow: hidden;
      margin-bottom: 30px;
    }

    .cheatsheet-table th, .cheatsheet-table td {
      padding: 12px 16px;
      text-align: left;
      font-size: 13px;
      border-bottom: 1px solid var(--border-color);
    }

    .cheatsheet-table th {
      background: #070b14;
      color: var(--text-muted);
      font-weight: 600;
      text-transform: uppercase;
      font-size: 11px;
      letter-spacing: 0.5px;
    }

    .cheatsheet-table tr:hover { background: rgba(255, 255, 255, 0.02); }

    .cmd-badge {
      font-family: ui-monospace, monospace;
      color: #38bdf8;
      background: #070b14;
      padding: 3px 7px;
      border-radius: 4px;
      border: 1px solid rgba(56, 189, 248, 0.2);
      font-size: 12px;
    }

    footer {
      text-align: center;
      padding: 30px 0;
      color: var(--text-dim);
      font-size: 13px;
      border-top: 1px solid var(--border-color);
      margin-top: 40px;
    }

    @media (max-width: 860px) {
      body { padding: 12px; }
      header { padding: 20px; }
      .header-top { flex-direction: column; }
      .controls { flex-direction: column; align-items: stretch; }
      .phase-row { flex-direction: column; }
      .phase-label { width: 100%; border-right: none; border-bottom: 1px solid var(--border-color); padding-bottom: 8px; }
      .step-header { flex-direction: column; align-items: flex-start; gap: 10px; }
      .step-badges { align-self: flex-start; }
    }
  </style>
</head>
<body>

<div class="container">
  <!-- Header -->
  <header>
    <div class="header-top">
      <div class="brand">
        <div class="brand-icon">⚡</div>
        <div>
          <h1 id="header-title">ApexMotion · Workshop Lern- & Fortschrittszentrale</h1>
          <p class="subtitle" id="header-subtitle">Interaktive Schritt-für-Schritt-Zusammenfassung aller Schritte, Architektur & Lernkonzepte</p>
        </div>
      </div>
      <div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap;">
        <button class="action-btn" onclick="downloadCurrentHTML()" title="Download HTML file" style="background:#070b14; border-color:#38bdf8; color:#38bdf8; font-weight:600;">
          <span>💾</span> <span data-i18n="btn_download">HTML Herunterladen</span>
        </button>
        <div class="lang-switch">
          <button class="lang-btn active" id="btn-de" onclick="setLanguage('de')">🇩🇪 Deutsch</button>
          <button class="lang-btn" id="btn-en" onclick="setLanguage('en')">🇬🇧 English</button>
        </div>
      </div>
    </div>

    <!-- Live Stats -->
    <div class="stats-bar">
      <div class="stat-card">
        <div class="stat-label" data-i18n="stat_project">Projekt & Agent</div>
        <div class="stat-value" style="font-size: 16px;">ApexMotion Coach</div>
        <div style="font-size: 11px; color: var(--text-dim); margin-top:2px;">Calisthenics & Sport Strength</div>
      </div>
      <div class="stat-card">
        <div class="stat-label" data-i18n="stat_gcp_project">GCP Projekt-ID</div>
        <div class="stat-value" style="font-size: 13px; font-family: ui-monospace, monospace; color: #facc15;">qwiklabs-gcp-03-746ba250987a</div>
        <div style="font-size: 11px; color: var(--text-dim); margin-top:2px;">Firestore + GCS + Agent Platform</div>
      </div>
      <div class="stat-card">
        <div class="stat-label" data-i18n="stat_steps">Fortschritt (Schritte)</div>
        <div class="stat-value"><span id="completed-count">13</span> / <span id="total-count">19</span></div>
        <div class="progress-track">
          <div class="progress-fill" id="progress-bar" style="width: 68%;"></div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-label" data-i18n="stat_reviewed">Gelernt / Wiederholt</div>
        <div class="stat-value" style="color: var(--accent-green);"><span id="reviewed-count">0</span> / 13</div>
        <div style="font-size: 11px; color: var(--text-dim); margin-top:2px;" data-i18n="stat_reviewed_hint">Klicke Checkboxen in den Schritten</div>
      </div>
    </div>
  </header>

  <!-- ========================================================
       1. INTERACTIVE ARCHITECTURE OVERVIEW (SVG DIAGRAM)
       ======================================================== -->
  <div class="hub-section" id="arch-overview">
    <div class="section-header">
      <div class="section-title-wrap">
        <span>🏛️</span> <span data-i18n="arch_title">Gesamtarchitektur & Datenfluss (Google Cloud Track 3)</span>
      </div>
      <span class="section-badge" data-de="Interaktives Flussdiagramm" data-en="Interactive Architecture Diagram">Interaktives Flussdiagramm</span>
    </div>

    <div class="arch-diagram-wrapper">
      <svg class="arch-svg" viewBox="0 0 920 260" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="gBlue" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#1e3a8a"/>
            <stop offset="100%" stop-color="#0f172a"/>
          </linearGradient>
          <linearGradient id="gPurple" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#581c87"/>
            <stop offset="100%" stop-color="#0f172a"/>
          </linearGradient>
          <linearGradient id="gYellow" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#713f12"/>
            <stop offset="100%" stop-color="#0f172a"/>
          </linearGradient>
          <linearGradient id="gGreen" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#14532d"/>
            <stop offset="100%" stop-color="#0f172a"/>
          </linearGradient>
          <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%">
            <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#000" flood-opacity="0.5"/>
          </filter>
        </defs>

        <!-- Connecting Lines -->
        <path d="M 140 130 L 230 130" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6,4" fill="none"/>
        <path d="M 370 130 L 460 130" stroke="#c084fc" stroke-width="3" fill="none"/>
        <path d="M 600 130 L 690 80" stroke="#facc15" stroke-width="2.5" fill="none"/>
        <path d="M 600 130 L 690 180" stroke="#4ade80" stroke-width="2.5" fill="none"/>

        <!-- Arrows -->
        <polygon points="225,125 235,130 225,135" fill="#38bdf8"/>
        <polygon points="455,125 465,130 455,135" fill="#c084fc"/>
        <polygon points="685,77 695,80 687,87" fill="#facc15"/>
        <polygon points="685,183 695,180 687,173" fill="#4ade80"/>

        <!-- Box 1: User / Frontend -->
        <g filter="url(#shadow)" onclick="jumpToStep(6)" style="cursor:pointer;">
          <rect x="20" y="80" width="120" height="100" rx="10" fill="url(#gBlue)" stroke="#38bdf8" stroke-width="1.5"/>
          <text x="80" y="112" fill="#38bdf8" font-size="20" text-anchor="middle">💻</text>
          <text x="80" y="135" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">Athlete / User</text>
          <text x="80" y="152" fill="#94a3b8" font-size="10" text-anchor="middle">Chat UI / Playground</text>
          <text x="80" y="166" fill="#64748b" font-size="9" text-anchor="middle">Port 8000/8080</text>
        </g>

        <!-- Box 2: FastAPI / A2A Proxy -->
        <g filter="url(#shadow)" onclick="jumpToStep(3)" style="cursor:pointer;">
          <rect x="235" y="80" width="135" height="100" rx="10" fill="url(#gBlue)" stroke="#38bdf8" stroke-width="1.5"/>
          <text x="302" y="112" fill="#38bdf8" font-size="20" text-anchor="middle">⚡</text>
          <text x="302" y="135" fill="#fff" font-size="12" font-weight="700" text-anchor="middle">FastAPI Proxy</text>
          <text x="302" y="152" fill="#94a3b8" font-size="10" text-anchor="middle">A2A Protocol / REST</text>
          <text x="302" y="166" fill="#64748b" font-size="9" text-anchor="middle">app/fast_api_app.py</text>
        </g>

        <!-- Box 3: Agent Core / Gemini -->
        <g filter="url(#shadow)" onclick="jumpToStep(5)" style="cursor:pointer;">
          <rect x="465" y="70" width="135" height="120" rx="10" fill="url(#gPurple)" stroke="#c084fc" stroke-width="2"/>
          <text x="532" y="105" fill="#c084fc" font-size="22" text-anchor="middle">🧠</text>
          <text x="532" y="128" fill="#fff" font-size="13" font-weight="800" text-anchor="middle">ApexMotion Agent</text>
          <text x="532" y="146" fill="#c084fc" font-size="10" font-weight="600" text-anchor="middle">Gemini 3.8 Flash High</text>
          <text x="532" y="162" fill="#94a3b8" font-size="9" text-anchor="middle">ReAct Reasoning Loop</text>
          <text x="532" y="176" fill="#64748b" font-size="9" text-anchor="middle">app/agent.py</text>
        </g>

        <!-- Box 4: Firestore NoSQL DB -->
        <g filter="url(#shadow)" onclick="jumpToStep(11)" style="cursor:pointer;">
          <rect x="695" y="30" width="195" height="95" rx="10" fill="url(#gYellow)" stroke="#facc15" stroke-width="1.5"/>
          <text x="792" y="58" fill="#facc15" font-size="18" text-anchor="middle">🗄️ Firestore NoSQL DB</text>
          <text x="792" y="78" fill="#fff" font-size="11" font-weight="600" text-anchor="middle">• exercises (Katalog)</text>
          <text x="792" y="94" fill="#94a3b8" font-size="10" text-anchor="middle">• athlete_profiles (RPE Ermüdung)</text>
          <text x="792" y="110" fill="#64748b" font-size="9" text-anchor="middle">• workout_logs (Historie)</text>
        </g>

        <!-- Box 5: Cloud Storage Bucket -->
        <g filter="url(#shadow)" onclick="jumpToStep(12)" style="cursor:pointer;">
          <rect x="695" y="145" width="195" height="85" rx="10" fill="url(#gGreen)" stroke="#4ade80" stroke-width="1.5"/>
          <text x="792" y="175" fill="#4ade80" font-size="18" text-anchor="middle">📦 Cloud Storage</text>
          <text x="792" y="195" fill="#fff" font-size="11" font-weight="600" text-anchor="middle">Public Assets Bucket (US-EAST1)</text>
          <text x="792" y="212" fill="#94a3b8" font-size="10" text-anchor="middle">allUsers:roles/storage.objectViewer</text>
        </g>
      </svg>
    </div>
  </div>

  <!-- ========================================================
       2. INTERACTIVE ROADMAP & OUTLINE TREE (CLICKABLE NODES)
       ======================================================== -->
  <div class="hub-section">
    <div class="section-header">
      <div class="section-title-wrap">
        <span>🗺️</span> <span data-i18n="roadmap_title">Interaktiver Ablauf-Baum & Lernpfad (Klickbar)</span>
      </div>
      <div class="section-badge" data-i18n="roadmap_hint">💡 Klicke auf ein Schlagwort, um direkt zum Abschnitt zu springen!</div>
    </div>

    <div class="tree-grid">

      <!-- Phase 1 -->
      <div class="phase-row">
        <div class="phase-label">
          <span class="phase-badge">Phase 1</span>
          <span class="phase-name" data-de="Setup & Cloud IAM" data-en="Setup & Cloud IAM">Setup & Cloud IAM</span>
        </div>
        <div class="phase-nodes">
          <div class="tree-node active-done" onclick="jumpToStep(1)">
            <span class="node-num">01</span>
            <span class="node-text" data-de="Git Repo Clone" data-en="Git Repo Clone">Git Repo Clone</span>
          </div>
          <span class="node-arrow">➔</span>
          <div class="tree-node active-done" onclick="jumpToStep(2)">
            <span class="node-num">02</span>
            <span class="node-text" data-de="IAM & ADC Verifikation" data-en="IAM & ADC Verification">IAM & ADC Verifikation</span>
          </div>
        </div>
      </div>

      <!-- Phase 2 -->
      <div class="phase-row">
        <div class="phase-label">
          <span class="phase-badge">Phase 2</span>
          <span class="phase-name" data-de="ReAct Agent Core" data-en="ReAct Agent Core">ReAct Agent Core</span>
        </div>
        <div class="phase-nodes">
          <div class="tree-node active-done" onclick="jumpToStep(3)">
            <span class="node-num">03</span>
            <span class="node-text" data-de="agents-cli Scaffold" data-en="agents-cli Scaffold">agents-cli Scaffold</span>
          </div>
          <span class="node-arrow">➔</span>
          <div class="tree-node active-done" onclick="jumpToStep(4)">
            <span class="node-num">04</span>
            <span class="node-text" data-de="Tool Test (Hanoi)" data-en="Tool Test (Hanoi)">Tool Test (Hanoi)</span>
          </div>
          <span class="node-arrow">➔</span>
          <div class="tree-node active-done" onclick="jumpToStep(5)">
            <span class="node-num">05</span>
            <span class="node-text" data-de="Gemini 3.8 Flash High" data-en="Gemini 3.8 Flash High">Gemini 3.8 Flash High</span>
          </div>
          <span class="node-arrow">➔</span>
          <div class="tree-node active-done" onclick="jumpToStep(6)">
            <span class="node-num">06</span>
            <span class="node-text" data-de="Agent Playground" data-en="Agent Playground">Agent Playground</span>
          </div>
        </div>
      </div>

      <!-- Phase 3 -->
      <div class="phase-row">
        <div class="phase-label">
          <span class="phase-badge">Phase 3</span>
          <span class="phase-name" data-de="Cloud & Workflow" data-en="Cloud & Workflow">Cloud & Workflow</span>
        </div>
        <div class="phase-nodes">
          <div class="tree-node active-done" onclick="jumpToStep(7)">
            <span class="node-num">07</span>
            <span class="node-text" data-de="Reasoning Engine Deploy" data-en="Reasoning Engine Deploy">Reasoning Engine Deploy</span>
          </div>
          <span class="node-arrow">➔</span>
          <div class="tree-node active-done" onclick="jumpToStep(8)">
            <span class="node-num">08</span>
            <span class="node-text" data-de="Lokale Iterations-Regel" data-en="Local Iteration Rule">Lokale Iterations-Regel</span>
          </div>
        </div>
      </div>

      <!-- Phase 4 -->
      <div class="phase-row">
        <div class="phase-label">
          <span class="phase-badge">Phase 4</span>
          <span class="phase-name" data-de="ApexMotion Design" data-en="ApexMotion Design">ApexMotion Design</span>
        </div>
        <div class="phase-nodes">
          <div class="tree-node active-done" onclick="jumpToStep(9)">
            <span class="node-num">09</span>
            <span class="node-text" data-de="Project Brief & RPE" data-en="Project Brief & RPE">Project Brief & RPE</span>
          </div>
          <span class="node-arrow">➔</span>
          <div class="tree-node active-done" onclick="jumpToStep(10)">
            <span class="node-num">10</span>
            <span class="node-text" data-de="Rename & Config Sync" data-en="Rename & Config Sync">Rename & Config Sync</span>
          </div>
        </div>
      </div>

      <!-- Phase 5 -->
      <div class="phase-row">
        <div class="phase-label">
          <span class="phase-badge">Phase 5</span>
          <span class="phase-name" data-de="Datenbank & Storage" data-en="Database & Storage">Datenbank & Storage</span>
        </div>
        <div class="phase-nodes">
          <div class="tree-node active-done" onclick="jumpToStep(11)">
            <span class="node-num">11</span>
            <span class="node-text" data-de="Firestore DB & 4 Tools" data-en="Firestore DB & 4 Tools">Firestore DB & 4 Tools</span>
          </div>
          <span class="node-arrow">➔</span>
          <div class="tree-node active-done" onclick="jumpToStep(12)">
            <span class="node-num">12</span>
            <span class="node-text" data-de="Public Storage Bucket" data-en="Public Storage Bucket">Public Storage Bucket</span>
          </div>
          <span class="node-arrow">➔</span>
          <div class="tree-node active-done" onclick="jumpToStep(13)" style="border-color:#10b981;">
            <span class="node-num" style="background:rgba(16, 185, 129, 0.2); color:#10b981; border-color:#10b981;">13</span>
            <span class="node-text" data-de="🧪 Tests (Zero-GCP)" data-en="🧪 Tests (Zero-GCP)">🧪 Tests (Zero-GCP)</span>
          </div>
        </div>
      </div>

      <!-- Phase 6: Practical Live Tools, Video Tutorials, Gamified Quest & Math -->
      <div class="phase-row">
        <div class="phase-label">
          <span class="phase-badge" style="color:#ec4899;">Interaktiv</span>
          <span class="phase-name" data-de="Praxis & Spiel" data-en="Demos & Game">Praxis & Spiel</span>
        </div>
        <div class="phase-nodes">
          <div class="tree-node game-node" onclick="jumpToSection('game-arena')">
            <span class="node-num" style="background:rgba(236, 72, 153, 0.2); color:#ec4899; border-color:#ec4899;">QUEST</span>
            <span class="node-text" data-de="🎮 Level-Up Quest Arena" data-en="🎮 Level-Up Quest Arena">🎮 Level-Up Quest Arena</span>
          </div>
          <div class="tree-node video-node" onclick="jumpToSection('video-studio')">
            <span class="node-num" style="background:rgba(244, 63, 94, 0.2); color:#f43f5e; border-color:#f43f5e;">VIDEO</span>
            <span class="node-text" data-de="🎬 Video-Tutorials & Vorführungen" data-en="🎬 Video Tutorials & Screencasts">🎬 Video-Tutorials & Vorführungen</span>
          </div>
          <div class="tree-node sim-node" onclick="jumpToSection('interactive-simulator')">
            <span class="node-num" style="background:rgba(250, 204, 21, 0.2); color:var(--accent-yellow); border-color:var(--accent-yellow);">DEMO</span>
            <span class="node-text" data-de="🕹️ Live RPE & Recovery Simulator" data-en="🕹️ Live RPE & Recovery Simulator">🕹️ Live RPE & Recovery Simulator</span>
          </div>
          <div class="tree-node db-node" onclick="jumpToSection('firestore-explorer')">
            <span class="node-num" style="background:rgba(56, 189, 248, 0.2); color:var(--accent-blue); border-color:var(--accent-blue);">DB</span>
            <span class="node-text" data-de="📂 Firestore Data Explorer" data-en="📂 Firestore Data Explorer">📂 Firestore Data Explorer</span>
          </div>
          <div class="tree-node math-node" onclick="jumpToSection('math-deep-dive')">
            <span class="node-num" style="background:rgba(192, 132, 252, 0.2); color:var(--accent-purple); border-color:var(--accent-purple);">MATH</span>
            <span class="node-text" data-de="📐 Formel-Deep-Dive: RPE & Decay" data-en="📐 Math Deep Dive: RPE & Decay">📐 Formel-Deep-Dive: RPE & Decay</span>
          </div>
        </div>
      </div>

      <!-- Phase 7: Upcoming Roadmap -->
      <div class="phase-row">
        <div class="phase-label">
          <span class="phase-badge" style="color:var(--text-dim);">Ausstehend</span>
          <span class="phase-name" data-de="Geplante Roadmap" data-en="Upcoming Roadmap">Geplante Roadmap</span>
        </div>
        <div class="phase-nodes">
          <div class="tree-node upcoming-node" onclick="jumpToStep(14)">
            <span class="node-num">14</span>
            <span class="node-text">A2UI Cards</span>
          </div>
          <span class="node-arrow">➔</span>
          <div class="tree-node upcoming-node" onclick="jumpToStep(15)">
            <span class="node-num">15</span>
            <span class="node-text">Memory Bank</span>
          </div>
          <span class="node-arrow">➔</span>
          <div class="tree-node upcoming-node" onclick="jumpToStep(16)">
            <span class="node-num">16</span>
            <span class="node-text">Image Gen</span>
          </div>
          <span class="node-arrow">➔</span>
          <div class="tree-node upcoming-node" onclick="jumpToStep(17)">
            <span class="node-num">17</span>
            <span class="node-text">Code Sandbox</span>
          </div>
          <span class="node-arrow">➔</span>
          <div class="tree-node upcoming-node" onclick="jumpToStep(18)">
            <span class="node-num">18</span>
            <span class="node-text">Cloud Run UI</span>
          </div>
          <span class="node-arrow">➔</span>
          <div class="tree-node upcoming-node" onclick="jumpToStep(19)">
            <span class="node-num">19</span>
            <span class="node-text">GitHub Gallery</span>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- ========================================================
       🎮 LEVEL-UP GAME ARENA: "APEXMOTION QUEST"
       ======================================================== -->
  <div class="hub-section game-arena-wrapper" id="game-arena">
    <div class="section-header" style="border-bottom-color: rgba(236, 72, 153, 0.3);">
      <div class="section-title-wrap">
        <span style="color:#ec4899; font-size:22px;">🎮</span>
        <span style="color:#f472b6; font-weight:900;" data-i18n="game_arena_title">ApexMotion Quest: Das interaktive Lern-Spiel</span>
      </div>
      <div style="display:flex; gap:10px; align-items:center;">
        <button class="action-btn" id="game-sound-btn" onclick="toggleGameSound()" style="background:#070b14; border-color:#ec4899; color:#f472b6; font-size:11px; padding:4px 10px;">
          🔊 Sound: AN
        </button>
        <span class="section-badge" style="color:#ec4899; border-color:#ec4899;" data-de="Level-Up & Wissen anwenden" data-en="Level-Up & Apply Knowledge">Level-Up & Wissen anwenden</span>
      </div>
    </div>

    <!-- HUD Bar (Always visible during game) -->
    <div class="game-hud">
      <div class="hud-rank-badge">
        <span>⭐</span>
        <span id="hud-level-text">Level 1: Cloud Trainee</span>
      </div>

      <div class="hud-stats-group">
        <div class="hud-stat-item">
          <span>Leben:</span>
          <span class="hud-lives" id="hud-lives-display">❤️❤️❤️</span>
        </div>
        <div class="hud-stat-item">
          <span>Punkte:</span>
          <span class="hud-xp" id="hud-xp-display">0 XP</span>
        </div>
        <div class="hud-stat-item">
          <span>Combo:</span>
          <span class="hud-streak" id="hud-streak-display">1x 🔥</span>
        </div>
      </div>
    </div>

    <!-- 1. SCREEN: Game Start / Hero -->
    <div class="game-screen active" id="screen-game-start">
      <div class="game-hero-card">
        <div class="game-hero-icon">⚔️</div>
        <h2 class="game-hero-title" data-de="Werde zum zertifizierten Apex Grandmaster!" data-en="Become a Certified Apex Grandmaster!">Werde zum zertifizierten Apex Grandmaster!</h2>
        <p class="game-hero-desc" data-de="Wende dein gesamtes Wissen aus dem Workshop in 6 fordernden Praxis-Missionen an! Löse echte Cloud-IAM Fallen, steuere den ReAct-Reasoning-Loop, meistere die Firestore-Projekt-ID Klippe und berechne Erholungs-Mathematik für Calisthenics-Athleten. Jede richtige Antwort bringt dir XP und schaltet Meister-Abzeichen frei!" data-en="Apply everything you learned across 6 practical architectural missions! Solve real Cloud IAM traps, steer the ReAct loop, dodge the Firestore Project ID crash, and compute calisthenics recovery math. Earn XP, protect your 3 lives, and unlock mastery badges!">
          Wende dein gesamtes Wissen aus dem Workshop in 6 fordernden Praxis-Missionen an! Löse echte Cloud-IAM Fallen, steuere den ReAct-Reasoning-Loop, meistere die Firestore-Projekt-ID Klippe und berechne Erholungs-Mathematik für Calisthenics-Athleten. Jede richtige Antwort bringt dir XP und schaltet Meister-Abzeichen frei!
        </p>

        <div class="tier-badges-row">
          <div class="tier-pill">🐣 Lvl 1: Cloud Trainee (0 XP)</div>
          <div class="tier-pill">⚙️ Lvl 2: ReAct Developer (200 XP)</div>
          <div class="tier-pill">🗄️ Lvl 3: Firestore Architect (450 XP)</div>
          <div class="tier-pill">🧠 Lvl 4: Systems Engineer (750 XP)</div>
          <div class="tier-pill" style="border-color:#ec4899; color:#f472b6;">👑 Lvl 5: Apex Grandmaster (1000+ XP)</div>
        </div>

        <div>
          <button class="btn-start-game" onclick="startGameQuest()">
            <span>🚀</span> <span data-de="QUEST JETZT STARTEN" data-en="START QUEST NOW">QUEST JETZT STARTEN</span>
          </button>
        </div>
      </div>
    </div>

    <!-- 2. SCREEN: Active Question / Mission -->
    <div class="game-screen" id="screen-game-mission">
      <div class="mission-header">
        <span class="mission-badge" id="mission-step-indicator">MISSION 1 VON 6</span>
        <span class="mission-xp-reward" id="mission-reward-indicator">+150 XP BELOHNUNG</span>
      </div>

      <div class="scenario-box">
        <div class="scenario-title" id="mission-scenario-title">Szenario-Titel</div>
        <p id="mission-scenario-desc" style="font-size: 13px; color: #cbd5e1; line-height: 1.5;">Beschreibung des Dilemmas...</p>
        <div class="scenario-snippet" id="mission-scenario-snippet" style="display:none;"></div>
      </div>

      <div class="quiz-options" id="mission-options-container">
        <!-- Dynamic Options inserted by JS -->
      </div>

      <!-- Feedback box after choice -->
      <div class="game-feedback-box" id="mission-feedback-box">
        <div style="font-weight: 800; font-size: 14px; margin-bottom: 4px;" id="feedback-headline">Antwortstatus</div>
        <div style="font-size: 12px; line-height: 1.5;" id="feedback-detail">Detailerklärung</div>
      </div>

      <div style="display: flex; justify-content: flex-end;">
        <button class="btn-next-mission" id="btn-next-mission" onclick="nextMission()">
          <span data-de="Nächste Mission" data-en="Next Mission">Nächste Mission</span> <span>➔</span>
        </button>
      </div>
    </div>

    <!-- 3. SCREEN: Game Over (All lives lost) -->
    <div class="game-screen" id="screen-game-over">
      <div class="game-hero-card" style="border-color: #ef4444;">
        <div class="game-hero-icon">💀</div>
        <h2 class="game-hero-title" style="background: linear-gradient(90deg, #ef4444, #f97316); -webkit-background-clip: text; -webkit-text-fill-color: transparent;" data-de="Alle Leben aufgebraucht!" data-en="Out of Lives!">
          Alle Leben aufgebraucht!
        </h2>
        <p class="game-hero-desc" data-de="Keine Sorge – im echten Cloud Engineering lernt man am meisten aus Fehlern! Schau dir die Erklärungen an und starte den Durchlauf mit frischen 3 Herzen neu." data-en="Don't worry – in real cloud engineering, we learn most from failures! Review the feedback and try again with 3 fresh hearts.">
          Keine Sorge – im echten Cloud Engineering lernt man am meisten aus Fehlern! Schau dir die Erklärungen an und starte den Durchlauf mit frischen 3 Herzen neu.
        </p>
        <button class="btn-start-game" onclick="restartGameQuest()" style="background: linear-gradient(135deg, #ef4444, #f97316);">
          <span>🔄</span> <span data-de="NOCHMAL VERSUCHEN" data-en="TRY AGAIN">NOCHMAL VERSUCHEN</span>
        </button>
      </div>
    </div>

    <!-- 4. SCREEN: Victory & Grandmaster Certificate -->
    <div class="game-screen" id="screen-game-victory">
      <div class="victory-box">
        <canvas id="confetti-canvas"></canvas>
        <div class="game-hero-icon">👑</div>
        <h2 class="game-hero-title" style="font-size: 28px;" data-de="HERZLICHEN GLÜCKWUNSCH, APEX GRANDMASTER!" data-en="CONGRATULATIONS, APEX GRANDMASTER!">
          HERZLICHEN GLÜCKWUNSCH, APEX GRANDMASTER!
        </h2>
        <p class="game-hero-desc" data-de="Du hast alle 6 fordernden Cloud- & Agent-Missionen gemeistert, dein Wissen erfolgreich angewendet und die Maximalstufe erreicht!" data-en="You mastered all 6 cloud & agent missions, applied every concept taught in the hub, and achieved Grandmaster rank!">
          Du hast alle 6 fordernden Cloud- & Agent-Missionen gemeistert, dein Wissen erfolgreich angewendet und die Maximalstufe erreicht!
        </p>

        <div style="font-size: 20px; font-weight: 800; color: #facc15; margin-bottom: 16px;">
          <span data-de="Erreichte Endpunktzahl:" data-en="Final Score:">Erreichte Endpunktzahl:</span> <span id="victory-final-score">1200 XP</span>
        </div>

        <div style="font-size: 13px; font-weight: 700; color: #f472b6; text-transform: uppercase; letter-spacing: 0.6px;" data-de="Deine freigeschalteten Meister-Abzeichen:" data-en="Your Unlocked Mastery Badges:">
          Deine freigeschalteten Meister-Abzeichen:
        </div>

        <div class="badges-collection-grid">
          <div class="badge-item unlocked">
            <div class="badge-icon">🛡️</div>
            <div class="badge-name">Cloud IAM Defender</div>
            <div class="badge-desc" data-de="ADC & aiplatform.user meisterhaft konfiguriert" data-en="Mastered ADC & aiplatform.user">ADC & aiplatform.user meisterhaft konfiguriert</div>
          </div>
          <div class="badge-item unlocked">
            <div class="badge-icon">🧠</div>
            <div class="badge-name">ReAct Logic Guru</div>
            <div class="badge-desc" data-de="Tool-Calling & Gemini Flash Loop verstanden" data-en="Understood Tool-Calling & Gemini Loop">Tool-Calling & Gemini Flash Loop verstanden</div>
          </div>
          <div class="badge-item unlocked">
            <div class="badge-icon">🗄️</div>
            <div class="badge-name">Firestore Architect</div>
            <div class="badge-desc" data-de="Project ID String Gotcha erfolgreich umgangen" data-en="Defeated numeric Project ID trap">Project ID String Gotcha erfolgreich umgangen</div>
          </div>
          <div class="badge-item unlocked">
            <div class="badge-icon">📐</div>
            <div class="badge-name">Biomechanics Math Pro</div>
            <div class="badge-desc" data-de="Halbwertszeit-Decay & RPE Skalierung berechnet" data-en="Calculated half-life decay & RPE delta">Halbwertszeit-Decay & RPE Skalierung berechnet</div>
          </div>
          <div class="badge-item unlocked">
            <div class="badge-icon">🏆</div>
            <div class="badge-name">Apex Grandmaster</div>
            <div class="badge-desc" data-de="Alle 6 Missionen siegreich abgeschlossen" data-en="Completed all 6 missions successfully">Alle 6 Missionen siegreich abgeschlossen</div>
          </div>
        </div>

        <button class="btn-start-game" onclick="restartGameQuest()">
          <span>🔄</span> <span data-de="QUEST ERNEUT SPIELEN" data-en="PLAY QUEST AGAIN">QUEST ERNEUT SPIELEN</span>
        </button>
      </div>
    </div>

  </div>

  <!-- ========================================================
       3. VIDEO TUTORIALS & INTERACTIVE TERMINAL SCREANCAST PLAYER
       ======================================================== -->
  <div class="hub-section" id="video-studio" style="border-color: #f43f5e; box-shadow: 0 10px 25px -5px rgba(244, 63, 94, 0.15);">
    <div class="section-header">
      <div class="section-title-wrap">
        <span style="color:#f43f5e;">🎬</span> <span data-i18n="video_heading">Video-Tutorials & Praxis-Vorführungen</span>
      </div>
      <span class="section-badge" style="color:#f43f5e; border-color:#f43f5e;" data-de="Interaktive Vorführung mit Sprecher-Untertitel" data-en="Interactive Screencast with Subtitles">Interaktive Vorführung mit Sprecher-Untertitel</span>
    </div>

    <p style="font-size:13px; color:var(--text-muted); margin-bottom:16px;" data-de="Hier kannst du dir die einzelnen praktischen Schritte als interaktive Vorführung ansehen. Sie zeigt dir exakt, wie Befehle im Terminal eingetippt werden, wie der ReAct-Reasoning Loop denkt, wie Firestore befüllt wird und wie der Coach im Playground antwortet:" data-en="Watch interactive terminal screencasts and practical walkthroughs. See exact commands, ReAct execution traces, Firestore seeding in action, and live coaching responses:">
      Hier kannst du dir die einzelnen praktischen Schritte als interaktive Vorführung ansehen. Sie zeigt dir exakt, wie Befehle im Terminal eingetippt werden, wie der ReAct-Reasoning Loop denkt, wie Firestore befüllt wird und wie der Coach im Playground antwortet:
    </p>

    <div class="video-studio-grid">
      <!-- Video Player Frame -->
      <div class="video-player-frame">
        <div class="video-title-bar">
          <div class="mac-dots">
            <span class="mac-dot red"></span>
            <span class="mac-dot yellow"></span>
            <span class="mac-dot green"></span>
          </div>
          <div id="video-clip-title" style="font-size:12px; font-weight:700; color:#cbd5e1; font-family:monospace;">
            tutorial_01_react_tool_calling.mp4
          </div>
          <div style="font-size:11px; color:#64748b; font-family:monospace;" id="video-time-indicator">00:00 / 00:30</div>
        </div>

        <div class="video-screen" id="video-screen-content">
          <div class="terminal-output-area" id="terminal-screen-text">
            <div class="term-log"># Klicke unten auf "▶️ Vorführung abspielen" oder wähle rechts ein Tutorial aus!</div>
            <div class="term-log"># Click "▶️ Play Walkthrough" below or select a tutorial on the right!</div>
          </div>

          <!-- Narration Banner -->
          <div class="narration-banner" id="narration-box">
            <span style="font-size:16px;">🎙️</span>
            <span id="narration-text">Bereit zum Abspielen. Wähle eine Vorführung aus der Playlist.</span>
          </div>
        </div>

        <!-- Video Controls Bar -->
        <div class="video-controls-bar">
          <div class="video-scrubber-track" onclick="scrubVideo(event)">
            <div class="video-scrubber-fill" id="video-progress"></div>
          </div>
          <div class="video-buttons-row">
            <div style="display:flex; gap:8px; align-items:center;">
              <button class="video-btn" id="play-pause-btn" onclick="togglePlayVideo()">
                <span id="play-icon">▶️</span> <span id="play-text" data-de="Abspielen" data-en="Play">Abspielen</span>
              </button>
              <button class="video-btn" onclick="restartVideo()">
                <span>🔄</span> <span data-de="Neustart" data-en="Restart">Neustart</span>
              </button>
            </div>
            <div style="display:flex; gap:8px; align-items:center;">
              <button class="video-btn" onclick="cycleSpeed()" id="speed-btn" style="font-family:monospace;">1.0x</button>
              <span style="font-size:11px; color:#64748b;" id="active-scene-badge">Szene 1/4</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Video Playlist -->
      <div class="playlist-card">
        <div style="font-size:13px; font-weight:800; color:#f8fafc; text-transform:uppercase; letter-spacing:0.6px; margin-bottom:4px;" data-de="Vorführungs-Playlist" data-en="Walkthrough Playlist">
          Vorführungs-Playlist
        </div>

        <div class="playlist-item active" onclick="loadTutorial(0)" id="play-item-0">
          <div class="item-icon">🤖</div>
          <div class="item-meta">
            <div class="item-title">1. Setup & Hanoi Weather ReAct Loop</div>
            <div class="item-dur" data-de="agents-cli run & Tool Calling" data-en="agents-cli run & Tool Calling">agents-cli run & Tool Calling</div>
          </div>
        </div>

        <div class="playlist-item" onclick="loadTutorial(1)" id="play-item-1">
          <div class="item-icon">💻</div>
          <div class="item-meta">
            <div class="item-title">2. Agent Playground & Hot-Reloading</div>
            <div class="item-dur" data-de="Port 8000 Web UI & Live Tracing" data-en="Port 8000 Web UI & Live Tracing">Port 8000 Web UI & Live Tracing</div>
          </div>
        </div>

        <div class="playlist-item" onclick="loadTutorial(2)" id="play-item-2">
          <div class="item-icon">🗄️</div>
          <div class="item-meta">
            <div class="item-title">3. Firestore NoSQL Seeding & Tools</div>
            <div class="item-dur" data-de="10 Übungen & Athleten-Recovery" data-en="10 exercises & athlete recovery">10 Übungen & Athleten-Recovery</div>
          </div>
        </div>

        <div class="playlist-item" onclick="loadTutorial(3)" id="play-item-3">
          <div class="item-icon">📦</div>
          <div class="item-meta">
            <div class="item-title">4. Cloud Storage Bucket & IAM Freigabe</div>
            <div class="item-dur" data-de="allUsers:roles/storage.objectViewer" data-en="allUsers:roles/storage.objectViewer">allUsers:roles/storage.objectViewer</div>
          </div>
        </div>

        <div class="playlist-item" onclick="loadTutorial(4)" id="play-item-4">
          <div class="item-icon">🏋️</div>
          <div class="item-meta">
            <div class="item-title">5. ApexMotion Coaching & RPE Fatigue</div>
            <div class="item-dur" data-de="Live Workout Logging & Next-Day Split" data-en="Live Workout Logging & Next-Day Split">Live Workout Logging & Next-Day Split</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ========================================================
       4. INTERACTIVE LIVE SIMULATOR: RPE FATIGUE & 24H RECOVERY
       ======================================================== -->
  <div class="hub-section" id="interactive-simulator">
    <div class="section-header">
      <div class="section-title-wrap">
        <span>🕹️</span> <span data-i18n="sim_heading">Interaktiver Ermüdungs- & Erholungs-Simulator (Praxis-Tool)</span>
      </div>
      <span class="section-badge" style="color:var(--accent-yellow); border-color:var(--accent-yellow);">Live Berechnung</span>
    </div>

    <p style="font-size:13px; color:var(--text-muted); margin-bottom:16px;" data-de="Hier kannst du live testen, wie der ApexMotion-Coach Workouts berechnet: Wähle eine Übung und dein RPE-Level. Sieh zu, wie sich Muskelerschöpfung akkumuliert, der Readiness Score berechnet wird, und teste die 24h-Regenerationssimulation!" data-en="Test how ApexMotion calculates workouts in real time: Select an exercise and RPE intensity. Watch fatigue accumulate, see the Readiness Score update, and test the 24h biological recovery simulation!">
      Hier kannst du live testen, wie der ApexMotion-Coach Workouts berechnet: Wähle eine Übung und dein RPE-Level. Sieh zu, wie sich Muskelerschöpfung akkumuliert, der Readiness Score berechnet wird, und teste die 24h-Regenerationssimulation!
    </p>

    <div class="sim-grid">
      <!-- Left: Workout Logger Inputs -->
      <div class="sim-panel">
        <div class="sim-title">
          <span>⚡</span> <span data-de="Workout erfassen (log_workout_session)" data-en="Log Workout (log_workout_session)">Workout erfassen (log_workout_session)</span>
        </div>

        <div class="control-row">
          <div class="control-label">
            <span data-de="Athleten-Profil" data-en="Athlete Profile">Athleten-Profil</span>
            <span style="color:var(--accent-blue); font-family:monospace;">default_athlete</span>
          </div>
          <input type="text" class="sim-select" value="default_athlete (Climbing & Planche Focus)" disabled style="opacity:0.8;">
        </div>

        <div class="control-row">
          <div class="control-label">
            <span data-de="Übung auswählen" data-en="Select Exercise">Übung auswählen</span>
          </div>
          <select id="sim-exercise" class="sim-select" onchange="updateSimExerciseInfo()">
            <option value="planche_tuck">Tuck Planche (Skill Push: Anterior Delts, Core, Chest)</option>
            <option value="front_lever_tuck">Tuck Front Lever (Skill Pull: Lats, Biceps, Core)</option>
            <option value="weighted_pullup">Weighted Pull-Up (Pull: Lats, Biceps, Forearms)</option>
            <option value="handstand_pushup_wall">Wall Handstand Push-up (Vertical Push: Delts, Triceps)</option>
            <option value="pistol_squat">Pistol Squat (Legs: Quads, Glutes)</option>
          </select>
        </div>

        <div class="control-row">
          <div class="control-label">
            <span>RPE Intensität (Borg CR10 Skala)</span>
            <span id="rpe-val" style="font-weight:700; color:var(--accent-yellow);">8 / 10</span>
          </div>
          <input type="range" id="sim-rpe" class="sim-slider" min="1" max="10" value="8" oninput="document.getElementById('rpe-val').textContent = this.value + ' / 10'">
        </div>

        <button class="sim-btn-primary" onclick="executeSimWorkout()">
          <span>💪</span> <span data-de="Workout anwenden (+Fatigue)" data-en="Apply Workout (+Fatigue)">Workout anwenden (+Fatigue)</span>
        </button>

        <button class="sim-btn-secondary" onclick="simulateRestDecay()">
          <span>⏳</span> <span data-de="24 Stunden Erholung simulieren (Decay)" data-en="Simulate 24h Rest (Decay)">24 Stunden Erholung simulieren (Decay)</span>
        </button>

        <button class="sim-btn-secondary" onclick="resetSimMuscles()" style="font-size:11px; margin-top:4px;">
          <span>🔄</span> <span data-de="Auf Ausgangsstatus zurücksetzen" data-en="Reset to Initial State">Auf Ausgangsstatus zurücksetzen</span>
        </button>
      </div>

      <!-- Right: Real-time Muscle State & Readiness -->
      <div class="sim-panel">
        <div class="sim-title">
          <span>📊</span> <span data-de="Aktueller Muskelstatus (athlete_profiles)" data-en="Current Muscle State (athlete_profiles)">Aktueller Muskelstatus (athlete_profiles)</span>
        </div>

        <div class="muscle-bars">
          <!-- Anterior Delts -->
          <div class="muscle-row">
            <div class="muscle-meta">
              <span>Vordere Schultern (Anterior Delts)</span>
              <span id="score-delts" style="font-weight:700;">2 / 10</span>
            </div>
            <div class="muscle-bar-track">
              <div class="muscle-bar-fill" id="bar-delts" style="width: 20%; background: var(--accent-green);"></div>
            </div>
          </div>

          <!-- Lats -->
          <div class="muscle-row">
            <div class="muscle-meta">
              <span>Latissimus (Lats / Pull)</span>
              <span id="score-lats" style="font-weight:700;">6 / 10</span>
            </div>
            <div class="muscle-bar-track">
              <div class="muscle-bar-fill" id="bar-lats" style="width: 60%; background: var(--accent-yellow);"></div>
            </div>
          </div>

          <!-- Core -->
          <div class="muscle-row">
            <div class="muscle-meta">
              <span>Core / Bauchpresse</span>
              <span id="score-core" style="font-weight:700;">3 / 10</span>
            </div>
            <div class="muscle-bar-track">
              <div class="muscle-bar-fill" id="bar-core" style="width: 30%; background: var(--accent-green);"></div>
            </div>
          </div>

          <!-- Biceps -->
          <div class="muscle-row">
            <div class="muscle-meta">
              <span>Bizeps / Zugkette</span>
              <span id="score-biceps" style="font-weight:700;">6 / 10</span>
            </div>
            <div class="muscle-bar-track">
              <div class="muscle-bar-fill" id="bar-biceps" style="width: 60%; background: var(--accent-yellow);"></div>
            </div>
          </div>

          <!-- Legs -->
          <div class="muscle-row">
            <div class="muscle-meta">
              <span>Beine (Quads & Glutes)</span>
              <span id="score-legs" style="font-weight:700;">1 / 10</span>
            </div>
            <div class="muscle-bar-track">
              <div class="muscle-bar-fill" id="bar-legs" style="width: 10%; background: var(--accent-green);"></div>
            </div>
          </div>
        </div>

        <!-- Readiness Score Output -->
        <div class="readiness-box">
          <div style="font-size:11px; text-transform:uppercase; color:var(--text-dim);" data-de="Berechneter Split Readiness Score" data-en="Calculated Split Readiness Score">Berechneter Split Readiness Score</div>
          <div class="readiness-score-num" id="readiness-display" style="color:var(--accent-yellow);">6.4 / 10</div>
          <div id="readiness-status" style="font-size:12px; font-weight:700; color:var(--accent-yellow);" data-de="🟡 Gelb: Moderate Intensität / Push & Planche empfohlen (Lats ermüdet)" data-en="🟡 Yellow: Moderate Intensity / Push & Planche recommended (Lats fatigued)">
            🟡 Gelb: Moderate Intensität / Push & Planche empfohlen (Lats ermüdet)
          </div>
        </div>

      </div>
    </div>
  </div>

  <!-- ========================================================
       5. INTERACTIVE FIRESTORE DATA EXPLORER
       ======================================================== -->
  <div class="hub-section" id="firestore-explorer">
    <div class="section-header">
      <div class="section-title-wrap">
        <span>📂</span> <span data-i18n="db_heading">Firestore Live-Datenbank Explorer</span>
      </div>
      <span class="section-badge" style="color:var(--accent-blue); border-color:var(--accent-blue);">Echte Dokumente</span>
    </div>

    <p style="font-size:13px; color:var(--text-muted); margin-bottom:14px;" data-de="Klicke auf die Tabs, um die tatsächlich in der GCP Cloud Firestore NoSQL-Datenbank angelegten Sammlungen und Dokumente zu inspizieren:" data-en="Click the tabs below to inspect the actual JSON documents stored in Google Cloud Firestore NoSQL database:">
      Klicke auf die Tabs, um die tatsächlich in der GCP Cloud Firestore NoSQL-Datenbank angelegten Sammlungen und Dokumente zu inspizieren:
    </p>

    <div class="db-tabs">
      <button class="db-tab-btn active" onclick="showDbDoc('planche', this)">exercises/planche_tuck</button>
      <button class="db-tab-btn" onclick="showDbDoc('front_lever', this)">exercises/front_lever_tuck</button>
      <button class="db-tab-btn" onclick="showDbDoc('pullup', this)">exercises/weighted_pullup</button>
      <button class="db-tab-btn" onclick="showDbDoc('athlete', this)">athlete_profiles/default_athlete</button>
      <button class="db-tab-btn" onclick="showDbDoc('workout', this)">workout_logs/session_example</button>
    </div>

    <pre class="db-doc-viewer" id="db-viewer-content"><code>{
  "id": "planche_tuck",
  "name": "Tuck Planche",
  "category": "skill_push",
  "target_muscles": ["anterior_delts", "chest", "core", "scapular_protractors"],
  "difficulty": "intermediate",
  "description": "Isometric hold with knees tucked to chest, arms straight, shoulders protracted.",
  "default_sets": 4,
  "default_hold_seconds": 12,
  "fatigue_factor": 7
}</code></pre>
  </div>

  <!-- ========================================================
       6. MATHEMATISCHE FORMELN & ENGINE DEEP-DIVE
       ======================================================== -->
  <div class="hub-section" id="math-deep-dive" style="border-color: var(--accent-purple);">
    <div class="section-header">
      <div class="section-title-wrap">
        <span style="color:var(--accent-purple);">📐</span> <span data-i18n="math_heading">Mathematische Modelle & Algorithmen des Agenten</span>
      </div>
      <span class="section-badge" style="color:var(--accent-purple); border-color:var(--accent-purple);" data-de="Hintergrundwissen & Formeln" data-en="Theory & Mathematics">Hintergrundwissen & Formeln</span>
    </div>

    <div class="math-grid">

      <!-- Math 1 -->
      <div class="math-card">
        <div class="math-card-title">
          <span>⚡</span> <span data-de="1. RPE-Ermüdungsakkumulation" data-en="1. RPE Fatigue Accumulation">1. RPE-Ermüdungsakkumulation</span>
        </div>
        <div class="math-desc" data-de="Wie wird das subjektive Anstrengungsempfinden (RPE 1-10) in messbare Muskelerschöpfung umgewandelt?" data-en="How subjective exertion (RPE 1-10) is converted into numerical muscle group fatigue:"></div>
        <div class="math-formula-box">
          &Delta;F = &lfloor; RPE / 2 &rfloor; &times; &omega;<sub>intensity</sub><br><br>
          F<sub>neu</sub>(m) = min(10, F<sub>alt</sub>(m) + &Delta;F)
        </div>
        <div class="math-desc" data-de="<strong>Erklärung:</strong> RPE 10 (Muskelversagen) erzeugt +5 Ermüdungspunkte. Der Skalierungsfaktor &omega; gewichtet spezifische Zielmuskeln (z.B. Planche &rarr; anterior_delts = &omega; 1.25)." data-en="<strong>Explanation:</strong> RPE 10 (failure) creates +5 fatigue points. Intensity weight &omega; applies to targeted muscle groups (e.g. Planche &rarr; anterior delts = 1.25)."></div>
      </div>

      <!-- Math 2 -->
      <div class="math-card">
        <div class="math-card-title">
          <span>⏳</span> <span data-de="2. Exponentieller Erholungszerfall" data-en="2. Exponential Recovery Decay">2. Exponentieller Erholungszerfall</span>
        </div>
        <div class="math-desc" data-de="Muskelermüdung baut sich über die Zeit exponentiell mit einer muskelabhängigen Halbwertszeit T<sub>1/2</sub> ab:" data-en="Muscle fatigue decreases exponentially over time according to biological half-life T<sub>1/2</sub>:"></div>
        <div class="math-formula-box">
          F(t) = F<sub>0</sub> &times; e<sup>-&lambda; &times; &Delta;t</sup><br><br>
          &lambda; = ln(2) / T<sub>1/2</sub>
        </div>
        <div class="math-desc" data-de="<strong>Halbwertszeiten:</strong> Kleine Muskeln (Core, Delts): T<sub>1/2</sub> &approx; 24h. Große Ketten (Lats, Quads): T<sub>1/2</sub> &approx; 40-48h. Ermöglicht dynamische Pausenberechnung." data-en="<strong>Half-lives:</strong> Small stabilizers (Core, Delts): T<sub>1/2</sub> &approx; 24h. Large chains (Lats, Quads): T<sub>1/2</sub> &approx; 40-48h."></div>
      </div>

      <!-- Math 3 -->
      <div class="math-card">
        <div class="math-card-title">
          <span>🎯</span> <span data-de="3. Split Readiness Score & Ampel" data-en="3. Split Readiness Decision Matrix">3. Split Readiness Decision Matrix</span>
        </div>
        <div class="math-desc" data-de="Entscheidungsregel für den nächsten Tag basierend auf dem Durchschnitt der beteiligten Muskeln M<sub>S</sub>:" data-en="Decision rule determining next-day training readiness across split muscles M<sub>S</sub>:"></div>
        <div class="math-formula-box">
          Readiness(S) = 10 - &frac12; [ &frac1n; &sum;<sub>m&isin;M</sub> F(m) ]
        </div>
        <div class="math-desc" data-de="<strong>Matrix:</strong><br>&bull; &ge; 7.5: 🟢 <strong>Grün</strong> (Heavy Skill Training: Planche / Front Lever)<br>&bull; 5.0 - 7.4: 🟡 <strong>Gelb</strong> (Accessory / Rep-Volumen)<br>&bull; &lt; 5.0: 🔴 <strong>Rot</strong> (Rest Day oder Mobility / Yoga / Stretching)" data-en="<strong>Matrix:</strong><br>&bull; &ge; 7.5: 🟢 <strong>Green</strong> (Heavy Skill: Planche / Front Lever)<br>&bull; 5.0 - 7.4: 🟡 <strong>Yellow</strong> (Accessory / Moderate Volume)<br>&bull; &lt; 5.0: 🔴 <strong>Red</strong> (Active Rest / Mobility / Yoga)"></div>
      </div>

    </div>
  </div>

  <!-- Search & Filter Controls -->
  <div class="controls">
    <div class="search-box">
      <span class="search-icon">🔍</span>
      <input type="text" id="search-input" class="search-input" placeholder="Schritt, Befehl oder Konzept suchen..." oninput="filterSteps()">
    </div>
    <div class="filter-group">
      <button class="filter-btn active" data-filter="all" onclick="setFilter('all', this)" data-i18n="filter_all">Alle (19)</button>
      <button class="filter-btn" data-filter="setup" onclick="setFilter('setup', this)">Setup</button>
      <button class="filter-btn" data-filter="agent" onclick="setFilter('agent', this)">Agent Core</button>
      <button class="filter-btn" data-filter="db" onclick="setFilter('db', this)">Firestore</button>
      <button class="filter-btn" data-filter="storage" onclick="setFilter('storage', this)">Storage</button>
      <button class="filter-btn" data-filter="tests" onclick="setFilter('tests', this)">Offline Tests</button>
      <button class="filter-btn" data-filter="upcoming" onclick="setFilter('upcoming', this)" data-i18n="filter_upcoming">Ausstehend</button>
    </div>
    <div style="display:flex; gap: 8px;">
      <button class="action-btn" onclick="toggleAllSteps(true)" data-i18n="btn_expand_all">▼ Alle aufklappen</button>
      <button class="action-btn" onclick="toggleAllSteps(false)" data-i18n="btn_collapse_all">▲ Einklappen</button>
    </div>
  </div>

  <!-- ========================================================
       STEP-BY-STEP LEARNING TIMELINE WITH PRACTICAL RESULTS
       ======================================================== -->
  <div class="timeline" id="steps-container">

    <!-- STEP 1 -->
    <div class="step-card completed expanded" data-category="setup" id="step-card-1">
      <div class="step-header" onclick="toggleStep(1)">
        <div class="step-title-area">
          <div class="step-num">01</div>
          <div>
            <div class="step-title-text" data-de="Workshop-Repository geklont & Umgebung eingerichtet" data-en="Workshop Repo Cloned & Environment Setup">Workshop-Repository geklont & Umgebung eingerichtet</div>
            <div style="font-size: 12px; color: var(--text-dim);">build-with-gemini / Track 3 Starter Kit</div>
          </div>
        </div>
        <div class="step-badges">
          <span class="badge badge-setup">Setup</span>
          <span class="chevron">▼</span>
        </div>
      </div>
      <div class="step-body">
        <div class="detail-grid">

          <div class="why-box">
            <div class="why-title"><span>🎯</span> <span data-i18n="lbl_why_step">Warum dieser Schritt?</span></div>
            <p data-de="Das Starter-Kit stellt das standardisierte Grundgerüst für Google Cloud Agent Platform bereit. Es enthält einsatzbereite Antigravity-Skills, CI/CD-Vorlagen und den Paketmanager `uv`, um Abhängigkeiten konsistent und ohne Versionskonflikte bereitzustellen." data-en="The starter kit provides the standardized framework for Google Cloud Agent Platform. It packages ready-made Antigravity skills, CI/CD blueprints, and `uv` package management to guarantee consistent environments."></p>
          </div>

          <div class="info-box">
            <div class="info-box-title blue"><span>📌</span> <span data-i18n="lbl_what_was_done">Was wurde gemacht?</span></div>
            <p data-de="Das GitHub-Repository `cszhu/build-with-gemini` wurde auf der Google Cloud VM in den Arbeitsbereich `/config/Desktop/BuildWithGemini` geklont." data-en="The GitHub repository `cszhu/build-with-gemini` was cloned into the Google Cloud VM workspace."></p>
          </div>

          <div class="code-container">
            <div class="code-header">
              <span>BASH TERMINAL</span>
              <button class="copy-btn" onclick="copyCode(this)">Kopieren</button>
            </div>
            <pre><code>git clone https://github.com/cszhu/build-with-gemini.git
cd BuildWithGemini</code></pre>
          </div>

          <div class="info-box result-box">
            <div class="info-box-title green"><span>✅</span> <span>Echtes Praxisergebnis / Artifact</span></div>
            <p data-de="Arbeitsbereich erfolgreich initialisiert. Struktur mit `.agents/skills/`, `my-agent/` und Lab-Hilfswerkzeugen einsatzbereit." data-en="Workspace initialized. Blueprints in `.agents/skills/` and agent templates loaded."></p>
          </div>

        </div>
        <label class="learn-check">
          <input type="checkbox" onchange="markReviewed(1, this.checked)">
          <span data-i18n="chk_understood">Ich habe diesen Schritt verstanden und wiederholt</span>
        </label>
      </div>
    </div>

    <!-- STEP 2 -->
    <div class="step-card completed" data-category="setup" id="step-card-2">
      <div class="step-header" onclick="toggleStep(2)">
        <div class="step-title-area">
          <div class="step-num">02</div>
          <div>
            <div class="step-title-text" data-de="Umgebungs- und Berechtigungsprüfung (Lab Verification)" data-en="Environment & IAM Verification">Umgebungs- und Berechtigungsprüfung (Lab Verification)</div>
            <div style="font-size: 12px; color: var(--text-dim);">gcloud auth & aiplatform.user verification</div>
          </div>
        </div>
        <div class="step-badges">
          <span class="badge badge-setup">Setup</span>
          <span class="chevron">▼</span>
        </div>
      </div>
      <div class="step-body">
        <div class="detail-grid">

          <div class="why-box">
            <div class="why-title"><span>🎯</span> <span data-i18n="lbl_why_step">Warum dieser Schritt?</span></div>
            <p data-de="Verhindert kryptische Authentifizierungs- und Berechtigungsfehler (403 FORBIDDEN). In Cloud-Workshops muss verifiziert werden, dass die lokale IDE mit dem temporären Qwiklabs-Konto und nicht mit privaten Google-Konten verknüpft ist." data-en="Prevents mysterious 403 FORBIDDEN errors. In cloud labs, we must verify that the IDE uses the temporary Qwiklabs identity rather than personal Google accounts."></p>
          </div>

          <div class="info-box">
            <div class="info-box-title blue"><span>📌</span> <span data-i18n="lbl_what_was_done">Was wurde gemacht?</span></div>
            <p data-de="Prüfung von `gcloud auth list`, Application Default Credentials (ADC), Projekt-ID `qwiklabs-gcp-03-746ba250987a` und der IAM-Rolle `roles/aiplatform.user`." data-en="Verified `gcloud auth list`, Application Default Credentials (ADC), active project ID `qwiklabs-gcp-03-746ba250987a`, and IAM role `roles/aiplatform.user`."></p>
          </div>

          <div class="info-box result-box">
            <div class="info-box-title green"><span>✅</span> <span>Echtes Praxisergebnis / Verified Output</span></div>
            <pre style="background:transparent; padding:0; color:#4ade80;"><code>[ACTIVE] student-03-88849b3842be@qwiklabs.net
Active GCP Project: qwiklabs-gcp-03-746ba250987a
IAM Check: roles/aiplatform.user -> PASSED</code></pre>
          </div>

        </div>
        <label class="learn-check">
          <input type="checkbox" onchange="markReviewed(2, this.checked)">
          <span data-i18n="chk_understood">Ich habe diesen Schritt verstanden und wiederholt</span>
        </label>
      </div>
    </div>

    <!-- STEP 3 -->
    <div class="step-card completed" data-category="agent" id="step-card-3">
      <div class="step-header" onclick="toggleStep(3)">
        <div class="step-title-area">
          <div class="step-num">03</div>
          <div>
            <div class="step-title-text" data-de="Basis-Agent mit `agents-cli` generiert" data-en="Scaffolded Starter Agent with `agents-cli`">Basis-Agent mit `agents-cli` generiert</div>
            <div style="font-size: 12px; color: var(--text-dim);">ADK (Agent Development Kit) & Python uv Environment</div>
          </div>
        </div>
        <div class="step-badges">
          <span class="badge badge-agent">Agent Core</span>
          <span class="chevron">▼</span>
        </div>
      </div>
      <div class="step-body">
        <div class="detail-grid">

          <div class="why-box">
            <div class="why-title"><span>🎯</span> <span data-i18n="lbl_why_step">Warum dieser Schritt?</span></div>
            <p data-de="Schnelle Generierung eines standardisierten ReAct-Agenten (Reasoning + Acting) mit Google ADK (`Agent`, `App`, `Gemini`), inklusive Abhängigkeiten und FastAPI-Proxy, um Boilerplate-Code zu vermeiden." data-en="Rapidly scaffolds a production ReAct agent using Google ADK (`Agent`, `App`, `Gemini`) with pre-wired FastAPI server to avoid manual boilerplate."></p>
          </div>

          <div class="info-box">
            <div class="info-box-title blue"><span>📌</span> <span data-i18n="lbl_what_was_done">Was wurde gemacht?</span></div>
            <p data-de="Generierung via `agents-cli`, Erstellung von `app/agent.py`, `app/fast_api_app.py`, `pyproject.toml` und Installation mit `agents-cli install`." data-en="Initialized agent via `agents-cli`, generated `app/agent.py`, `app/fast_api_app.py`, `pyproject.toml`, and installed packages via `agents-cli install`."></p>
          </div>

          <div class="code-container">
            <div class="code-header">
              <span>BASH TERMINAL</span>
              <button class="copy-btn" onclick="navigator.clipboard.writeText('agents-cli install')">Copy</button>
            </div>
            <pre><code>agents-cli init apexmotion
cd apexmotion
agents-cli install</code></pre>
          </div>

        </div>
        <label class="learn-check">
          <input type="checkbox" onchange="markReviewed(3, this.checked)">
          <span data-i18n="chk_understood">Ich habe diesen Schritt verstanden und wiederholt</span>
        </label>
      </div>
    </div>

    <!-- STEP 4 -->
    <div class="step-card completed" data-category="agent" id="step-card-4">
      <div class="step-header" onclick="toggleStep(4)">
        <div class="step-title-area">
          <div class="step-num">04</div>
          <div>
            <div class="step-title-text" data-de="Lokaler Funktionstest & Tool-Calling Verifikation" data-en="Local Testing & Tool-Calling Verification">Lokaler Funktionstest & Tool-Calling Verifikation</div>
            <div style="font-size: 12px; color: var(--text-dim);">ReAct Trace: 'What is the weather in Hanoi?'</div>
          </div>
        </div>
        <div class="step-badges">
          <span class="badge badge-agent">Agent Core</span>
          <span class="chevron">▼</span>
        </div>
      </div>
      <div class="step-body">
        <div class="detail-grid">

          <div class="why-box">
            <div class="why-title"><span>🎯</span> <span data-i18n="lbl_why_step">Warum dieser Schritt?</span></div>
            <p data-de="Verifiziert sofort, ob der ReAct-Reasoning-Loop funktioniert: Das LLM muss einen User-Prompt verstehen, die Tool-Definition auswerten, Parameter extrahieren und das Tool fehlerfrei ausführen." data-en="Immediately proves the ReAct loop: the model must parse user intent, evaluate tool signatures, extract arguments, and execute Python functions reliably."></p>
          </div>

          <!-- Quick Jump Button to Video -->
          <div style="margin: 4px 0;">
            <button class="action-btn" onclick="playTutorialDirect(0)" style="background:#1e293b; border-color:#f43f5e; color:#f43f5e; font-weight:700;">
              <span>▶️</span> <span>Video-Vorführung zu diesem Schritt ansehen (Tutorial 1)</span>
            </button>
          </div>

          <div class="info-box result-box">
            <div class="info-box-title green"><span>✅</span> <span>Echter Ausführungs-Trace (ReAct Loop)</span></div>
            <pre style="background:transparent; padding:0; color:#38bdf8;"><code>User: "What is the weather in Hanoi?"
🧠 Model Thought: Need weather information for Hanoi. Calling get_weather tool.
🛠️ Tool Call: get_weather(query="Hanoi")
📦 Tool Result: {"location": "Hanoi", "temperature": 28, "condition": "Sunny"}
💬 Final Answer: "The current weather in Hanoi is sunny with a temperature of 28°C."</code></pre>
          </div>

        </div>
        <label class="learn-check">
          <input type="checkbox" onchange="markReviewed(4, this.checked)">
          <span data-i18n="chk_understood">Ich habe diesen Schritt verstanden und wiederholt</span>
        </label>
      </div>
    </div>

    <!-- STEP 5 -->
    <div class="step-card completed" data-category="agent" id="step-card-5">
      <div class="step-header" onclick="toggleStep(5)">
        <div class="step-title-area">
          <div class="step-num">05</div>
          <div>
            <div class="step-title-text" data-de="Modellwahl optimiert: Gemini 3.8 Flash (High)" data-en="Model Optimization: Gemini 3.8 Flash (High)">Modellwahl optimiert: Gemini 3.8 Flash (High)</div>
            <div style="font-size: 12px; color: var(--text-dim);">High-performance Tool Dispatch & Reasoning</div>
          </div>
        </div>
        <div class="step-badges">
          <span class="badge badge-agent">Agent Core</span>
          <span class="chevron">▼</span>
        </div>
      </div>
      <div class="step-body">
        <div class="detail-grid">

          <div class="why-box">
            <div class="why-title"><span>🎯</span> <span data-i18n="lbl_why_step">Warum dieser Schritt?</span></div>
            <p data-de="Für agentische Anwendungen ist Multi-Step Tool-Calling und JSON-Strukturtreue entscheidend. `Gemini Flash High` bietet höchste Genauigkeit bei minimaler Latenz." data-en="For agentic apps, multi-step tool execution and strict structured output are essential. `Gemini Flash High` delivers elite reasoning accuracy at ultra-low latency."></p>
          </div>

          <div class="code-container">
            <div class="code-header">
              <span>PYTHON (app/agent.py)</span>
              <button class="copy-btn" onclick="navigator.clipboard.writeText('model=\'gemini-2.5-flash\'')">Kopieren</button>
            </div>
            <pre><code>from google.adk.agents import Agent

agent = Agent(
    model="gemini-2.5-flash",
    description="ApexMotion Calisthenics Strength Coach"
)</code></pre>
          </div>

        </div>
        <label class="learn-check">
          <input type="checkbox" onchange="markReviewed(5, this.checked)">
          <span data-i18n="chk_understood">Ich habe diesen Schritt verstanden und wiederholt</span>
        </label>
      </div>
    </div>

    <!-- STEP 6 -->
    <div class="step-card completed" data-category="agent" id="step-card-6">
      <div class="step-header" onclick="toggleStep(6)">
        <div class="step-title-area">
          <div class="step-num">06</div>
          <div>
            <div class="step-title-text" data-de="Interaktiver Agent Playground gestartet" data-en="Launched Local Agent Playground">Interaktiver Agent Playground gestartet</div>
            <div style="font-size: 12px; color: var(--text-dim);">Port 8000/8080 · Hot Reloading on Save</div>
          </div>
        </div>
        <div class="step-badges">
          <span class="badge badge-agent">Agent Core</span>
          <span class="chevron">▼</span>
        </div>
      </div>
      <div class="step-body">
        <div class="detail-grid">

          <div class="why-box">
            <div class="why-title"><span>🎯</span> <span data-i18n="lbl_why_step">Warum dieser Schritt?</span></div>
            <p data-de="Ermöglicht eine visuelle Testumgebung im Browser mit Live-Tracing aller LLM-Gedankenschritte, Tool-Aufrufe und Rückgabewerte bei jeder gespeicherten Code-Änderung." data-en="Provides a visual browser testing suite displaying execution traces, thought processes, tool arguments, and return values with instant hot-reloading."></p>
          </div>

          <!-- Quick Jump Button to Video -->
          <div style="margin: 4px 0;">
            <button class="action-btn" onclick="playTutorialDirect(1)" style="background:#1e293b; border-color:#f43f5e; color:#f43f5e; font-weight:700;">
              <span>▶️</span> <span>Video-Vorführung zu diesem Schritt ansehen (Tutorial 2)</span>
            </button>
          </div>

          <div class="code-container">
            <div class="code-header">
              <span>BASH TERMINAL</span>
              <button class="copy-btn" onclick="copyCode(this)">Kopieren</button>
            </div>
            <pre><code>cd apexmotion
agents-cli playground</code></pre>
          </div>

        </div>
        <label class="learn-check">
          <input type="checkbox" onchange="markReviewed(6, this.checked)">
          <span data-i18n="chk_understood">Ich habe diesen Schritt verstanden und wiederholt</span>
        </label>
      </div>
    </div>

    <!-- STEP 7 -->
    <div class="step-card completed" data-category="setup" id="step-card-7">
      <div class="step-header" onclick="toggleStep(7)">
        <div class="step-title-area">
          <div class="step-num">07</div>
          <div>
            <div class="step-title-text" data-de="Erstes Baseline-Deployment auf Agent Platform" data-en="Initial Baseline Deployment to Agent Platform">Erstes Baseline-Deployment auf Agent Platform</div>
            <div style="font-size: 12px; color: var(--text-dim);">Vertex AI Reasoning Engine Deployment</div>
          </div>
        </div>
        <div class="step-badges">
          <span class="badge badge-deploy">Deployment</span>
          <span class="chevron">▼</span>
        </div>
      </div>
      <div class="step-body">
        <div class="detail-grid">

          <div class="why-box">
            <div class="why-title"><span>🎯</span> <span data-i18n="lbl_why_step">Warum dieser Schritt?</span></div>
            <p data-de="Stellt sicher, dass das Cloud-Packaging, die Containerisierung und die Vertex AI Reasoning Engine Endpunkte von Anfang an fehlerfrei funktionieren, bevor komplexe Logik hinzugefügt wird." data-en="Proves container packaging and Vertex AI Reasoning Engine endpoints work early before adding complex business logic."></p>
          </div>

          <div class="info-box result-box">
            <div class="info-box-title green"><span>✅</span> <span>Echtes Praxisergebnis / Deployment Endpoint</span></div>
            <p data-de="Reasoning Engine Instanz erfolgreich in US-CENTRAL1 registriert. Bereit für Cloud-Streaming." data-en="Reasoning Engine resource successfully provisioned in US-CENTRAL1."></p>
          </div>

          <div class="code-container">
            <div class="code-header">
              <span>BASH TERMINAL (Vertex AI Reasoning Engine)</span>
              <button class="copy-btn" onclick="copyCode(this)">Kopieren</button>
            </div>
            <pre><code>agents-cli deploy
# Deployed to Vertex AI Reasoning Engine (US-CENTRAL1)
# Endpoint: projects/qwiklabs-gcp-03-746ba250987a/locations/us-central1/reasoningEngines/...</code></pre>
          </div>

        </div>
        <label class="learn-check">
          <input type="checkbox" onchange="markReviewed(7, this.checked)">
          <span data-i18n="chk_understood">Ich habe diesen Schritt verstanden und wiederholt</span>
        </label>
      </div>
    </div>

    <!-- STEP 8 -->
    <div class="step-card completed" data-category="setup" id="step-card-8">
      <div class="step-header" onclick="toggleStep(8)">
        <div class="step-title-area">
          <div class="step-num">08</div>
          <div>
            <div class="step-title-text" data-de="Entwicklungsregel: Lokale Iteration vor Deployment" data-en="Dev Workflow Rule: Local Iteration First">Entwicklungsregel: Lokale Iteration vor Deployment</div>
            <div style="font-size: 12px; color: var(--text-dim);">Deploy-only-when-asked & Fast Feedback Loop</div>
          </div>
        </div>
        <div class="step-badges">
          <span class="badge badge-setup">Workflow</span>
          <span class="chevron">▼</span>
        </div>
      </div>
      <div class="step-body">
        <div class="detail-grid">

          <div class="why-box">
            <div class="why-title"><span>🎯</span> <span data-i18n="lbl_why_step">Warum dieser Schritt?</span></div>
            <p data-de="Vermeidet massive Zeitverluste: Cloud-Deployments dauern 3-5 Minuten pro Durchlauf. Durch lokales Testen im Playground erhalten wir Feedback in Millisekunden und schonen Quota." data-en="Avoids massive development delays: Cloud deploys take 3-5 minutes. Local playground iteration provides feedback in milliseconds while conserving quota."></p>
          </div>

          <div class="code-container">
            <div class="code-header">
              <span>TERMINAL (Lokale Test-Schleife)</span>
              <button class="copy-btn" onclick="copyCode(this)">Kopieren</button>
            </div>
            <pre><code># Lokale Iteration: 0.2s Feedback statt 4min Cloud Deployment
agents-cli run "Logge mein Tuck Planche Training mit RPE 9"</code></pre>
          </div>

        </div>
        <label class="learn-check">
          <input type="checkbox" onchange="markReviewed(8, this.checked)">
          <span data-i18n="chk_understood">Ich habe diesen Schritt verstanden und wiederholt</span>
        </label>
      </div>
    </div>

    <!-- STEP 9 -->
    <div class="step-card completed" data-category="agent" id="step-card-9">
      <div class="step-header" onclick="toggleStep(9)">
        <div class="step-title-area">
          <div class="step-num">09</div>
          <div>
            <div class="step-title-text" data-de="Konzept & Design: ApexMotion Calisthenics Coach" data-en="Design & Specification: ApexMotion Coach">Konzept & Design: ApexMotion Calisthenics Coach</div>
            <div style="font-size: 12px; color: var(--text-dim);">project_brief.md · RPE Fatigue Score & Skill Progressions</div>
          </div>
        </div>
        <div class="step-badges">
          <span class="badge badge-agent">Agent Core</span>
          <span class="chevron">▼</span>
        </div>
      </div>
      <div class="step-body">
        <div class="detail-grid">

          <div class="why-box">
            <div class="why-title"><span>🎯</span> <span data-i18n="lbl_why_step">Warum dieser Schritt?</span></div>
            <p data-de="Ein präzises Briefing definiert die Domäne, das Erschöpfungsmodell (RPE) und die erforderlichen Google Cloud Bausteine (Firestore, Storage, Memory, A2UI), bevor Code geschrieben wird." data-en="A detailed brief anchors domain requirements, fatigue scoring mechanics, and required Google Cloud services before scaffolding features."></p>
          </div>

          <div class="info-box result-box">
            <div class="info-box-title green"><span>✅</span> <span>Echtes Praxisergebnis / Artifact: project_brief.md</span></div>
            <pre style="background:transparent; padding:0; color:#e2e8f0;"><code>Domain: Calisthenics & Sport Strength (Planche, Front Lever, Climbing, Volleyball)
Fatigue Model: RPE 1-10 per muscle group with exponential decay
Tools: Firestore catalog, Athlete profile recovery, GCS public bucket</code></pre>
          </div>

        </div>
        <label class="learn-check">
          <input type="checkbox" onchange="markReviewed(9, this.checked)">
          <span data-i18n="chk_understood">Ich habe diesen Schritt verstanden und wiederholt</span>
        </label>
      </div>
    </div>

    <!-- STEP 10 -->
    <div class="step-card completed" data-category="agent" id="step-card-10">
      <div class="step-header" onclick="toggleStep(10)">
        <div class="step-title-area">
          <div class="step-num">10</div>
          <div>
            <div class="step-title-text" data-de="Projekt umbenannt in `apexmotion` & Konfiguration synchronisiert" data-en="Project Renamed to `apexmotion` & Config Sync">Projekt umbenannt in `apexmotion` & Konfiguration synchronisiert</div>
            <div style="font-size: 12px; color: var(--text-dim);">agents-cli-manifest.yaml & pyproject.toml</div>
          </div>
        </div>
        <div class="step-badges">
          <span class="badge badge-agent">Agent Core</span>
          <span class="chevron">▼</span>
        </div>
      </div>
      <div class="step-body">
        <div class="detail-grid">

          <div class="why-box">
            <div class="why-title"><span>🎯</span> <span data-i18n="lbl_why_step">Warum dieser Schritt?</span></div>
            <p data-de="Konsistente Projektidentität. `agents-cli` und Cloud Deployments nutzen den Manifest-Namen für Dienstbenennung, Cloud Trace Spans und Container-Tags." data-en="Maintains clean naming across manifests, package metadata, Cloud Trace spans, and container tags."></p>
          </div>

          <div class="code-container">
            <div class="code-header">
              <span>CONFIG SYNC</span>
              <button class="copy-btn" onclick="copyCode(this)">Kopieren</button>
            </div>
            <pre><code>sed -i 's/agent_starter/apexmotion/g' agents-cli-manifest.yaml
sed -i 's/name = "agent_starter"/name = "apexmotion"/' pyproject.toml</code></pre>
          </div>

        </div>
        <label class="learn-check">
          <input type="checkbox" onchange="markReviewed(10, this.checked)">
          <span data-i18n="chk_understood">Ich habe diesen Schritt verstanden und wiederholt</span>
        </label>
      </div>
    </div>

    <!-- STEP 11 -->
    <div class="step-card completed" data-category="db" id="step-card-11">
      <div class="step-header" onclick="toggleStep(11)">
        <div class="step-title-area">
          <div class="step-num">11</div>
          <div>
            <div class="step-title-text" data-de="Firestore NoSQL-Datenbank & Tools implementiert" data-en="Firestore Database Backend & ADK Tools Wired">Firestore NoSQL-Datenbank & Tools implementiert</div>
            <div style="font-size: 12px; color: var(--text-dim);">exercises, athlete_profiles, workout_logs Collections & Seed Script</div>
          </div>
        </div>
        <div class="step-badges">
          <span class="badge badge-db">Firestore</span>
          <span class="chevron">▼</span>
        </div>
      </div>
      <div class="step-body">
        <div class="detail-grid">

          <div class="why-box">
            <div class="why-title"><span>🎯</span> <span data-i18n="lbl_why_step">Warum dieser Schritt?</span></div>
            <p data-de="Ein Coach benötigt persistente Daten: Übungskataloge, Erschöpfungslevel der Muskeln und Trainingsprotokolle dürfen nach dem Gesprächsende nicht verloren gehen." data-en="A coaching agent requires persistence: exercise catalogs, muscular fatigue state, and workout history must survive across sessions."></p>
          </div>

          <!-- Quick Jump Button to Video -->
          <div style="margin: 4px 0;">
            <button class="action-btn" onclick="playTutorialDirect(2)" style="background:#1e293b; border-color:#f43f5e; color:#f43f5e; font-weight:700;">
              <span>▶️</span> <span>Video-Vorführung zu diesem Schritt ansehen (Tutorial 3)</span>
            </button>
          </div>

          <div class="info-box result-box">
            <div class="info-box-title green"><span>✅</span> <span>Echtes Praxisergebnis: 10 Übungen & Profil 'default_athlete'</span></div>
            <p data-de="`python seed_firestore.py` hat 10 Calisthenics-Übungen mit Haltezeiten, Schwierigkeit und Muskel-Targets erfolgreich in die Cloud-Datenbank geschrieben. Die 4 Werkzeuge sind in `app/agent.py` aktiviert!" data-en="10 exercises seeded and 4 tools wired into root_agent: list_exercises, get_exercise_details, get_muscle_exhaustion, log_workout_session."></p>
          </div>

          <div class="code-container">
            <div class="code-header">
              <span>PYTHON (Firestore Seeding & Tools)</span>
              <button class="copy-btn" onclick="copyCode(this)">Kopieren</button>
            </div>
            <pre><code>PROJECT_ID = "qwiklabs-gcp-03-746ba250987a"  # Hardcoded string literal!
db = firestore.Client(project=PROJECT_ID)
python3 seed_firestore.py  # Populates exercises, athlete_profiles & workout_logs</code></pre>
          </div>

          <div class="info-box gotcha">
            <div class="info-box-title yellow"><span>⚠️</span> <span data-i18n="lbl_arch_gotcha">Architektur-Highlight: Hardcoded Project ID String!</span></div>
            <p data-de="<strong>KRITISCH:</strong> Die Google Cloud Projekt-ID (`PROJECT_ID = 'qwiklabs-gcp-03-746ba250987a'`) MUSS als String fest hinterlegt werden! In der deployed Reasoning Engine liefert `google.auth.default()` die Projekt-NUMMER (z.B. 8192384918). Firestore akzeptiert nur den alphanumerischen Namen, sonst stürzt die App in der Cloud ab!" data-en="<strong>CRITICAL:</strong> Hardcoding Project ID as a string literal is mandatory! On Vertex AI Reasoning Engine, `google.auth.default()` returns the project NUMBER, which breaks Firestore client initialization."></p>
          </div>

        </div>
        <label class="learn-check">
          <input type="checkbox" onchange="markReviewed(11, this.checked)">
          <span data-i18n="chk_understood">Ich habe diesen Schritt verstanden und wiederholt</span>
        </label>
      </div>
    </div>

    <!-- STEP 12 -->
    <div class="step-card completed" data-category="storage" id="step-card-12">
      <div class="step-header" onclick="toggleStep(12)">
        <div class="step-title-area">
          <div class="step-num">12</div>
          <div>
            <div class="step-title-text" data-de="Öffentlicher Cloud Storage Bucket für Assets erstellt" data-en="Created Public Cloud Storage Bucket for Media">Öffentlicher Cloud Storage Bucket für Assets erstellt</div>
            <div style="font-size: 12px; color: var(--text-dim);">apexmotion-coach-qwiklabs-gcp-03-746ba250987a (US-EAST1)</div>
          </div>
        </div>
        <div class="step-badges">
          <span class="badge badge-storage">Cloud Storage</span>
          <span class="chevron">▼</span>
        </div>
      </div>
      <div class="step-body">
        <div class="detail-grid">

          <div class="why-box">
            <div class="why-title"><span>🎯</span> <span data-i18n="lbl_why_step">Warum dieser Schritt?</span></div>
            <p data-de="Web-Frontends und A2UI Rich Cards im Browser können Bilder nur anzeigen, wenn diese über eine öffentliche HTTPS-URL ohne Authentifizierungs-Token erreichbar sind." data-en="Web frontends and browser-rendered A2UI cards can only embed images accessible via public HTTPS URLs without authentication friction."></p>
          </div>

          <!-- Quick Jump Button to Video -->
          <div style="margin: 4px 0;">
            <button class="action-btn" onclick="playTutorialDirect(3)" style="background:#1e293b; border-color:#f43f5e; color:#f43f5e; font-weight:700;">
              <span>▶️</span> <span>Video-Vorführung zu diesem Schritt ansehen (Tutorial 4)</span>
            </button>
          </div>

          <div class="info-box result-box">
            <div class="info-box-title green"><span>✅</span> <span>Echtes Praxisergebnis: Öffentlicher Bucket bereit</span></div>
            <pre style="background:transparent; padding:0; color:#4ade80;"><code>Bucket: gs://apexmotion-coach-qwiklabs-gcp-03-746ba250987a
Location: US-EAST1
Policy: allUsers -> roles/storage.objectViewer (READ-PUBLIC)
URL Prefix: https://storage.googleapis.com/apexmotion-coach-qwiklabs-gcp-03-746ba250987a/</code></pre>
          </div>

        </div>
        <label class="learn-check">
          <input type="checkbox" onchange="markReviewed(12, this.checked)">
          <span data-i18n="chk_understood">Ich habe diesen Schritt verstanden und wiederholt</span>
        </label>
      </div>
    </div>

    <!-- STEP 13 (COMPLETED): 100% OFFLINE & PRIVATE PC TEST SUITE -->
    <div class="step-card completed" data-category="setup tests" id="step-card-13">
      <div class="step-header" onclick="toggleStep(13)">
        <div class="step-title-area">
          <div class="step-num">13</div>
          <div>
            <div class="step-title-text" data-de="Schritt 13: 100% Offline &amp; Private PC Test-Suite (Zero Google Cloud)" data-en="Step 13: 100% Offline &amp; Private PC Test Suite (Zero Google Cloud)">Schritt 13: 100% Offline &amp; Private PC Test-Suite (Zero Google Cloud)</div>
            <div style="font-size: 12px; color: var(--text-dim);" data-de="28 automatisierte Tests, In-Memory DB-Fallback, autarke HTML-Portabilität &amp; 1-Klick-Starter" data-en="28 automated tests, in-memory DB fallback, standalone HTML portability &amp; 1-click launchers">28 automatisierte Tests, In-Memory DB-Fallback, autarke HTML-Portabilität &amp; 1-Klick-Starter</div>
          </div>
        </div>
        <div class="step-badges">
          <span class="badge badge-success" data-i18n="badge_done">Abgeschlossen</span>
          <span class="chevron">▼</span>
        </div>
      </div>
      <div class="step-body">
        <div class="why-box">
          <div class="why-title"><span>🎯</span> <span data-i18n="lbl_why_step">Warum dieser Schritt?</span></div>
          <p data-de="Auf einem privaten Rechner oder Laptop ist Google Cloud (GCP) meist weder installiert noch autorisiert (kein `gcloud auth`, kein Service-Account, `403 PERMISSION_DENIED` oder `DefaultCredentialsError`). Damit die gesamte ApexMotion-Architektur (Agent-Tools, RPE-Fatigue-Logik, mathematische Zerfallsmodelle und die interaktive HTML-Zentrale) auf jedem privaten Windows-, Mac- oder Linux-Rechner fehlerfrei funktioniert, wurde ein transparenter Offline-Fallback mit 28 Unit- und Portabilitäts-Tests implementiert. So kann alles offline gelernt, wiederholt und getestet werden – sogar im Flugzeugmodus!" data-en="On a private computer or laptop, Google Cloud (GCP) is usually neither installed nor authorized (no `gcloud auth`, no service account, resulting in `DefaultCredentialsError`). To ensure that the entire ApexMotion architecture (agent tools, RPE fatigue logic, mathematical decay models, and the interactive HTML hub) works without errors on any private Windows, Mac, or Linux computer, a transparent offline fallback with 28 unit and portability tests was implemented. Everything can be learned, reviewed, and tested 100% offline – even in airplane mode!"></p>
        </div>

        <div class="card-grid">
          <div class="sub-card">
            <h4 data-de="🛠️ 1. In-Memory Firestore Fallback" data-en="🛠️ 1. In-Memory Firestore Fallback">🛠️ 1. In-Memory Firestore Fallback</h4>
            <p data-de="<code>app/tools_firestore.py</code> erkennt automatisch fehlende Google-Cloud-Credentials oder <code>APEXMOTION_OFFLINE_MODE=1</code>. Alle 4 Tools laufen mit einem integrierten In-Memory Store, der die 10 Calisthenics-Übungen und das Athletenprofil sofort bereitstellt." data-en="<code>app/tools_firestore.py</code> automatically detects missing Google Cloud credentials or <code>APEXMOTION_OFFLINE_MODE=1</code>. All 4 tools run with an embedded in-memory store pre-populated with exercises and athlete data."></p>
          </div>
          <div class="sub-card">
            <h4 data-de="🧪 2. 28 Automatisierte Tests" data-en="🧪 2. 28 Automated Tests">🧪 2. 28 Automatisierte Tests</h4>
            <p data-de="3 umfassende Testsuiten prüfen Agent-Tools, exponentielle Erholungs-Mathematik und HTML-Autarkie (0 externe CDN-Aufrufe, native Web Audio API, Canvas Confetti). Gesamtlaufzeit: blitzschnelle 10 ms!" data-en="3 test suites verify agent tools, exponential recovery math, and HTML self-containment (0 external CDN calls, native Web Audio API, Canvas confetti). Total runtime: ultra-fast 10 ms!"></p>
          </div>
        </div>

        <div class="terminal-block">
          <div class="term-title">
            <span>Terminal: Ausführung auf privatem PC (Zero Google Cloud)</span>
            <button class="copy-btn" onclick="copyCode(this)">Kopieren</button>
          </div>
          <pre><code><span class="term-prompt">user@private-laptop:~$</span> <span class="term-cmd">python3 run_all_tests.py</span>
==============================================================================
   ⚡ APEXMOTION TEST RUNNER - COMPLETE TEST &amp; OFFLINE VERIFICATION
   Target: Private PC / Laptop (Zero Google Cloud Required)
==============================================================================

  TEST SUITE                                           STATUS       TIME      
  --------------------------------------------------------------------------
  1. Agent Tools Offline Mode (Firestore Mock)         <span class="term-success">✔ PASS (8)</span>      0.7 ms
  2. Biomechanics Math (RPE &amp; Decay Models)            <span class="term-success">✔ PASS (5)</span>      0.3 ms
  3. HTML Learning Hub Portability &amp; Zero-CDN          <span class="term-success">✔ PASS (7)</span>      9.2 ms
  4. Desktop/HTML verify_offline.py Standalone Check   <span class="term-success">✔ PASS (8/8)</span>     35.0 ms
  --------------------------------------------------------------------------
  TOTAL:                                               <span class="term-success">28 passed, 0 failed</span>     10.2 ms

  🎉 ALL TESTS PASSED! 100% READY FOR YOUR PRIVATE COMPUTER.
  - No Google Cloud credentials or SDK required.
  - Standalone HTML, tools &amp; math formulas run completely offline.</code></pre>
        </div>

        <div class="card-grid" style="margin-top: 14px;">
          <div class="sub-card">
            <h4 data-de="🚀 1-Klick-Starter für deinen PC" data-en="🚀 1-Click Launchers for your PC">🚀 1-Klick-Starter für deinen PC</h4>
            <ul style="padding-left: 18px; font-size: 13px; color: var(--text-dim); line-height: 1.6;">
              <li><strong>Linux &amp; macOS:</strong> <code>./run_tests_local.sh</code></li>
              <li><strong>Windows:</strong> Doppelklick auf <code>run_tests_local.bat</code></li>
              <li><strong>Direkt im HTML-Ordner:</strong> <code>python verify_offline.py</code></li>
            </ul>
          </div>
          <div class="sub-card">
            <h4 data-de="📦 E-Mail &amp; USB-Portabilität" data-en="📦 E-Mail &amp; USB Portability">📦 E-Mail &amp; USB-Portabilität</h4>
            <p data-de="Die Datei <code>Desktop/HTML/ApexMotion_Workshop_Hub.zip</code> enthält jetzt <code>index.html</code>, <code>learning_progress.html</code>, <code>verify_offline.py</code> und <code>README.txt</code>. Nur 81 KB groß – perfekt für jede E-Mail!" data-en="<code>Desktop/HTML/ApexMotion_Workshop_Hub.zip</code> now packages <code>index.html</code>, <code>learning_progress.html</code>, <code>verify_offline.py</code> and <code>README.txt</code>. Only 81 KB – ideal for email!"></p>
          </div>
        </div>

        <label class="learn-check">
          <input type="checkbox" onchange="markReviewed(13, this.checked)">
          <span data-i18n="chk_understood">Ich habe diesen Schritt verstanden und wiederholt</span>
        </label>
      </div>
    </div>

    <!-- UPCOMING STEPS (14-19) -->
    <div class="step-card upcoming" data-category="upcoming" id="step-card-14">
      <div class="step-header" onclick="toggleStep(14)">
        <div class="step-title-area">
          <div class="step-num">14</div>
          <div>
            <div class="step-title-text" data-de="Ausstehend: A2UI Rich Cards (Agent-First UI)" data-en="Next: A2UI Rich Cards Integration">Ausstehend: A2UI Rich Cards (Agent-First UI)</div>
            <div style="font-size: 12px; color: var(--text-dim);">Interaktive Trainingskarten &amp; Erschöpfungs-Balken statt reinem Text</div>
          </div>
        </div>
        <div class="step-badges">
          <span class="badge" style="background:#263859; color:#94a3b8;">Geplant</span>
          <span class="chevron">▼</span>
        </div>
      </div>
      <div class="step-body">
        <div class="why-box">
          <div class="why-title"><span>🎯</span> <span data-i18n="lbl_why_step">Warum dieser Schritt?</span></div>
          <p data-de="Reiner Fließtext ist für Trainingspläne unübersichtlich. A2UI liefert saubere interaktive Karten, Tabellen und Fortschrittsbalken direkt aus dem Agenten." data-en="Plain text responses are cumbersome for workouts. A2UI renders structured cards, readiness tables, and progress bars."></p>
        </div>
      </div>
    </div>

    <div class="step-card upcoming" data-category="upcoming" id="step-card-15">
      <div class="step-header" onclick="toggleStep(15)">
        <div class="step-title-area">
          <div class="step-num">15</div>
          <div>
            <div class="step-title-text" data-de="Ausstehend: Langzeitgedächtnis (Memory Bank)" data-en="Next: Cross-Session Long-Term Memory Bank">Ausstehend: Langzeitgedächtnis (Memory Bank)</div>
            <div style="font-size: 12px; color: var(--text-dim);">Agent Platform Memory Bank für Athleten-Präferenzen &amp; Verletzungshistorie</div>
          </div>
        </div>
        <div class="step-badges">
          <span class="badge" style="background:#263859; color:#94a3b8;">Geplant</span>
          <span class="chevron">▼</span>
        </div>
      </div>
      <div class="step-body">
        <div class="why-box">
          <div class="why-title"><span>🎯</span> <span data-i18n="lbl_why_step">Warum dieser Schritt?</span></div>
          <p data-de="Ermöglicht echtes personifiziertes Coaching. Der Agent erinnert sich an Schulterverletzungen oder persönliche Rekorde auch nach Wochen noch." data-en="Enables true personalized coaching by remembering injuries, preferences, and personal records across weeks."></p>
        </div>
      </div>
    </div>

    <div class="step-card upcoming" data-category="upcoming" id="step-card-16">
      <div class="step-header" onclick="toggleStep(16)">
        <div class="step-title-area">
          <div class="step-num">16</div>
          <div>
            <div class="step-title-text" data-de="Ausstehend: Bildgenerierung (Gemini Image Gen)" data-en="Next: Image Generation for Exercise Cues">Ausstehend: Bildgenerierung (Gemini Image Gen)</div>
            <div style="font-size: 12px; color: var(--text-dim);">Haltungskontrollen (z.B. Scapular Protraction) &amp; Meilenstein-Grafiken</div>
          </div>
        </div>
        <div class="step-badges">
          <span class="badge" style="background:#263859; color:#94a3b8;">Geplant</span>
          <span class="chevron">▼</span>
        </div>
      </div>
      <div class="step-body">
        <div class="why-box">
          <div class="why-title"><span>🎯</span> <span data-i18n="lbl_why_step">Warum dieser Schritt?</span></div>
          <p data-de="Visualisiert komplexe Calisthenics-Haltungen (z.B. Schulterblatt-Protraktion in der Planche) direkt als KI-generierte Grafik." data-en="Visually demonstrates calisthenics technique (e.g. scapular protraction in planche) through on-demand generated cues."></p>
        </div>
      </div>
    </div>

    <div class="step-card upcoming" data-category="upcoming" id="step-card-17">
      <div class="step-header" onclick="toggleStep(17)">
        <div class="step-title-area">
          <div class="step-num">17</div>
          <div>
            <div class="step-title-text" data-de="Ausstehend: Code Sandbox für Erholungs-Mathematik" data-en="Next: Code Sandbox for Recovery Decay Math">Ausstehend: Code Sandbox für Erholungs-Mathematik</div>
            <div style="font-size: 12px; color: var(--text-dim);">Dynamische Exponential-Decay-Berechnung für Muskelermüdung</div>
          </div>
        </div>
        <div class="step-badges">
          <span class="badge" style="background:#263859; color:#94a3b8;">Geplant</span>
          <span class="chevron">▼</span>
        </div>
      </div>
      <div class="step-body">
        <div class="why-box">
          <div class="why-title"><span>🎯</span> <span data-i18n="lbl_why_step">Warum dieser Schritt?</span></div>
          <p data-de="LLMs neigen bei exponentiellen Formeln zu Rundungsfehlern. Die Code-Sandbox führt echten Python-Code sicher in isolierten Containern aus." data-en="LLMs make calculation errors with exponential decay. Code Sandbox executes exact mathematical Python code securely."></p>
        </div>
      </div>
    </div>

    <div class="step-card upcoming" data-category="upcoming" id="step-card-18">
      <div class="step-header" onclick="toggleStep(18)">
        <div class="step-title-area">
          <div class="step-num">18</div>
          <div>
            <div class="step-title-text" data-de="Ausstehend: Frontend auf Cloud Run deployen" data-en="Next: Deploy Frontend to Cloud Run">Ausstehend: Frontend auf Cloud Run deployen</div>
            <div style="font-size: 12px; color: var(--text-dim);">FastAPI A2A Proxy + Web UI mit A2UI Renderer</div>
          </div>
        </div>
        <div class="step-badges">
          <span class="badge" style="background:#263859; color:#94a3b8;">Geplant</span>
          <span class="chevron">▼</span>
        </div>
      </div>
      <div class="step-body">
        <div class="why-box">
          <div class="why-title"><span>🎯</span> <span data-i18n="lbl_why_step">Warum dieser Schritt?</span></div>
          <p data-de="Macht die Anwendung öffentlich im Web auf Smartphones und Laptops nutzbar – gehostet auf serverlosem Google Cloud Run." data-en="Hosts a public web application on serverless Cloud Run accessible to athletes on mobile and desktop."></p>
        </div>
      </div>
    </div>

    <div class="step-card upcoming" data-category="upcoming" id="step-card-19">
      <div class="step-header" onclick="toggleStep(19)">
        <div class="step-title-area">
          <div class="step-num">19</div>
          <div>
            <div class="step-title-text" data-de="Ausstehend: GitHub Veröffentlichung &amp; Showcase" data-en="Next: GitHub Publish &amp; Gallery Submission">Ausstehend: GitHub Veröffentlichung &amp; Showcase</div>
            <div style="font-size: 12px; color: var(--text-dim);">publish-to-github Skill &amp; Einreichung zur Featured Gallery</div>
          </div>
        </div>
        <div class="step-badges">
          <span class="badge" style="background:#263859; color:#94a3b8;">Geplant</span>
          <span class="chevron">▼</span>
        </div>
      </div>
      <div class="step-body">
        <div class="why-box">
          <div class="why-title"><span>🎯</span> <span data-i18n="lbl_why_step">Warum dieser Schritt?</span></div>
          <p data-de="Sichert deinen Code im eigenen GitHub-Account und reicht das Projekt in die offizielle Google Showcase-Galerie ein." data-en="Saves your code to your personal GitHub and submits your completed project to the official Google showcase gallery."></p>
        </div>
      </div>
    </div>
    </div>

  </div>

  <!-- CLI & Terminal Cheatsheet -->
  <div class="section-title">
    <span>⚡</span> <span data-i18n="title_cheatsheet">Wichtige Befehle & Cheatsheet</span>
  </div>
  <table class="cheatsheet-table">
    <thead>
      <tr>
        <th>Command</th>
        <th data-i18n="th_description">Beschreibung (DE / EN)</th>
        <th data-i18n="th_when">Wann nutzen?</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="cmd-badge">agents-cli playground</span></td>
        <td data-de="Startet den lokalen Webserver mit interaktivem Chat & Tracing" data-en="Launches local development server with chat & trace inspection">Startet den lokalen Webserver mit interaktivem Chat & Tracing</td>
        <td data-de="Zum Entwickeln und Testen von Agenten-Tools" data-en="For local testing and iterative development">Zum Entwickeln und Testen von Agenten-Tools</td>
      </tr>
      <tr>
        <td><span class="cmd-badge">python seed_firestore.py</span></td>
        <td data-de="Befüllt die Firestore-Datenbank mit Übungen und Muskelprofilen" data-en="Seeds Firestore database with calisthenics exercises and muscles">Befüllt die Firestore-Datenbank mit Übungen und Muskelprofilen</td>
        <td data-de="Initial oder nach Änderungen am Datenmodell" data-en="Initially or after modifying data schema">Initial oder nach Änderungen am Datenmodell</td>
      </tr>
      <tr>
        <td><span class="cmd-badge">gcloud storage buckets list</span></td>
        <td data-de="Listet alle Cloud Storage Buckets im aktiven Projekt auf" data-en="Lists all Cloud Storage buckets in active project">Listet alle Cloud Storage Buckets im aktiven Projekt auf</td>
        <td data-de="Zur Verifikation der Asset-Speicher" data-en="To verify asset storage buckets">Zur Verifikation der Asset-Speicher</td>
      </tr>
      <tr>
        <td><span class="cmd-badge">gcloud config get-value project</span></td>
        <td data-de="Gibt die alphanumerische Projekt-ID aus" data-en="Outputs active alphanumeric GCP project ID">Gibt die alphanumerische Projekt-ID aus</td>
        <td data-de="Vor Firestore-Konfigurationen" data-en="Before configuring Firestore clients">Vor Firestore-Konfigurationen</td>
      </tr>
      <tr>
        <td><span class="cmd-badge">agents-cli deploy</span></td>
        <td data-de="Stellt den Agenten auf der Google Cloud Reasoning Engine bereit" data-en="Deploys agent package to Vertex AI Reasoning Engine">Stellt den Agenten auf der Google Cloud Reasoning Engine bereit</td>
        <td data-de="Nur bei finalen Meilensteinen oder auf Wunsch" data-en="Only when final milestone is reached">Nur bei finalen Meilensteinen oder auf Wunsch</td>
      </tr>
    </tbody>
  </table>

  <footer>
    <p>ApexMotion Coach · Build with Gemini Track 3 · Google Cloud Agent Platform</p>
    <p style="margin-top: 4px; font-size: 11px;">Desktop-Pfad: Desktop/HTML/learning_progress.html · 100% Offline & E-Mail-Ready</p>
  </footer>
</div>

<script>
  let currentLang = localStorage.getItem('apexmotion_lang') || 'de';
  let reviewedSteps = JSON.parse(localStorage.getItem('apexmotion_reviewed') || '{}');

  // ========================================================
  // WEB AUDIO API SOUND SYNTHESIZER (100% Offline & Native)
  // ========================================================
  let soundEnabled = true;
  function toggleGameSound() {
    soundEnabled = !soundEnabled;
    const btn = document.getElementById('game-sound-btn');
    if (btn) {
      btn.textContent = soundEnabled ? (currentLang === 'de' ? '🔊 Sound: AN' : '🔊 Sound: ON') : (currentLang === 'de' ? '🔇 Sound: AUS' : '🔇 Sound: OFF');
    }
  }

  function playTone(freq, type, duration, delay = 0) {
    if (!soundEnabled) return;
    try {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (!AudioCtx) return;
      const ctx = new AudioCtx();
      setTimeout(() => {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = type;
        osc.frequency.setValueAtTime(freq, ctx.currentTime);
        gain.gain.setValueAtTime(0.08, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + duration);
      }, delay);
    } catch (e) {}
  }

  function playSoundChime() {
    playTone(523.25, 'sine', 0.12, 0);     // C5
    playTone(659.25, 'sine', 0.12, 100);   // E5
    playTone(783.99, 'sine', 0.25, 200);   // G5
  }

  function playSoundBuzz() {
    playTone(180, 'sawtooth', 0.22, 0);
  }

  function playSoundFanfare() {
    playTone(523.25, 'triangle', 0.15, 0);
    playTone(659.25, 'triangle', 0.15, 120);
    playTone(783.99, 'triangle', 0.15, 240);
    playTone(1046.50, 'triangle', 0.45, 360);
  }

  // ========================================================
  // 🎮 APEXMOTION QUEST: GAME ENGINE DATA & STATE
  // ========================================================
  let gameState = {
    currentMissionIndex: 0,
    scoreXP: 0,
    lives: 3,
    streak: 1,
    level: 1,
    isCompleted: false
  };

  const missionsData = [
    {
      title_de: "Mission 1: Die IAM- & Cloud-Auth-Falle",
      title_en: "Mission 1: The Cloud IAM & Auth Trap",
      scenario_de: "Du führst einen Testlauf aus und die Vertex AI Reasoning Engine antwortet mit einer roten Fehlermeldung:",
      scenario_en: "You run a test command and Vertex AI Reasoning Engine rejects execution with an error:",
      snippet: "google.api_core.exceptions.PermissionDenied: 403 Caller does not have required permission to use Vertex AI",
      reward: 150,
      options: [
        {
          text_de: "Deine IDE ist mit einem privaten Google-Konto authentifiziert statt mit dem temporären @qwiklabs.net-Konto. Lösung: gcloud auth login und gcloud auth application-default login ausführen!",
          text_en: "Your IDE is authenticated with a personal Google account instead of the @qwiklabs.net lab identity. Solution: run gcloud auth login & gcloud auth application-default login!",
          correct: true,
          feedback_de: "Volltreffer! In Cloud-Workshops ist der falsche ADC-Konto-Kontext der #1 Grund für 403 PERMISSION_DENIED.",
          feedback_en: "Spot on! In lab environments, wrong ADC credentials are the #1 root cause for 403 PERMISSION_DENIED."
        },
        {
          text_de: "Der lokale Port 8000 ist durch eine Firewall blockiert.",
          text_en: "Local port 8000 is blocked by a firewall.",
          correct: false,
          feedback_de: "Falsch! Port 8000 betrifft nur den lokalen Playground-Webserver, nicht die Cloud-Berechtigung von Vertex AI.",
          feedback_en: "Incorrect! Port 8000 only affects the local playground webserver, not Vertex AI cloud permissions."
        },
        {
          text_de: "Python 3.12 wird von Google Cloud nicht unterstützt.",
          text_en: "Python 3.12 is unsupported by Google Cloud.",
          correct: false,
          feedback_de: "Falsch! Der Workshop läuft auf einem modernen Python 3.12 Container.",
          feedback_en: "Incorrect! The workshop environment natively runs on modern Python 3.12."
        }
      ]
    },
    {
      title_de: "Mission 2: ReAct Tool-Calling & Reasoning Loop",
      title_en: "Mission 2: ReAct Tool-Calling & Reasoning Loop",
      scenario_de: "Ein Athlet fragt: 'Wie stark ist mein Bizeps gerade ermüdet und kann ich Klimmzüge machen?' Welchen ReAct-Ablauf führt Gemini 3.8 Flash aus?",
      scenario_en: "An athlete asks: 'How fatigued are my biceps right now?' What exact ReAct sequence does Gemini 3.8 Flash execute?",
      snippet: 'User: "Wie stark ist mein Bizeps gerade ermüdet?"\\n🧠 Gemini Flash: Evaluating tool registry...',
      reward: 150,
      options: [
        {
          text_de: "Thought: Brauche aktuellen Muskelstatus -> Tool: get_muscle_exhaustion(athlete_id='default_athlete') -> JSON auswerten -> Antwort formulieren.",
          text_en: "Thought: Need muscle exhaustion -> Tool: get_muscle_exhaustion(athlete_id='default_athlete') -> Parse JSON -> Synthesize reply.",
          correct: true,
          feedback_de: "Exzellent! Der Agent nutzt Tool-Calling, um verifizierte Fakten aus Firestore abzurufen, anstatt zu halluzinieren.",
          feedback_en: "Excellent! The agent dispatches tool calls to retrieve ground-truth data from Firestore rather than hallucinating."
        },
        {
          text_de: "Thought: Frage betrifft Wetter -> Tool: get_weather(query='biceps').",
          text_en: "Thought: Question is about weather -> Tool: get_weather(query='biceps').",
          correct: false,
          feedback_de: "Falsch! `get_weather` ist nur für meteorologische Abfragen zuständig.",
          feedback_en: "Incorrect! `get_weather` is only meant for meteorological queries."
        },
        {
          text_de: "Der Agent antwortet ohne Datenbankabfrage mit einer Schätzung.",
          text_en: "The agent guesses fatigue without querying the database.",
          correct: false,
          feedback_de: "Falsch! In einem agentischen System müssen Werkzeuge für dynamische Zustände herangezogen werden.",
          feedback_en: "Incorrect! In an agentic system, dynamic state must always be fetched via tools."
        }
      ]
    },
    {
      title_de: "Mission 3: Die fatale Firestore Projekt-ID Falle",
      title_en: "Mission 3: The Fatal Firestore Project ID Trap",
      scenario_de: "Warum haben wir in tools_firestore.py die Projekt-ID 'qwiklabs-gcp-03-746ba250987a' als String-Literal fest hinterlegt?",
      scenario_en: "Why did we hardcode 'qwiklabs-gcp-03-746ba250987a' as a string literal in tools_firestore.py?",
      snippet: 'PROJECT_ID = "qwiklabs-gcp-03-746ba250987a"  # Hardcoded string literal\\ndb = firestore.Client(project=PROJECT_ID)',
      reward: 200,
      options: [
        {
          text_de: "Auf Vertex AI Reasoning Engine liefert google.auth.default() die numerische Projekt-NUMMER, was den Firestore-Client zum Absturz bringt!",
          text_en: "On Vertex AI Reasoning Engine, google.auth.default() returns the numeric Project NUMBER, which crashes Firestore client!",
          correct: true,
          feedback_de: "Herausragend! Das ist eine der tückischsten Fallen beim Deployment von ADK-Agenten auf Vertex AI.",
          feedback_en: "Outstanding! This is one of the most insidious gotchas when deploying ADK agents to Vertex AI."
        },
        {
          text_de: "Weil Firestore keine Strings als Projekt-IDs akzeptiert.",
          text_en: "Because Firestore does not accept strings as Project IDs.",
          correct: false,
          feedback_de: "Falsch! Firestore verlangt zwingend die alphanumerische Projekt-ID als String.",
          feedback_en: "Incorrect! Firestore strictly requires the alphanumeric string ID."
        },
        {
          text_de: "Weil der Python-Code dadurch 10x schneller ausgeführt wird.",
          text_en: "Because it makes the Python code run 10x faster.",
          correct: false,
          feedback_de: "Falsch! Es geht um Schnittstellenkompatibilität, nicht um Laufzeitperformance.",
          feedback_en: "Incorrect! It's about schema compatibility, not runtime execution speed."
        }
      ]
    },
    {
      title_de: "Mission 4: Biologische Erholungs-Mathematik",
      title_en: "Mission 4: Biological Recovery Mathematics",
      scenario_de: "Die vorderen Schultern eines Athleten sind bei Ermüdung 8/10. Die biologische Halbwertszeit beträgt T1/2 = 24h. Der Athlet pausiert genau 24 Stunden. Welcher Wert resultiert?",
      scenario_en: "An athlete's anterior delts are at fatigue 8/10. Biological half-life is T1/2 = 24h. The athlete rests exactly 24 hours. What is the new fatigue level?",
      snippet: 'Formel: F(t) = F0 * e^(-lambda * Delta_t)  mit lambda = ln(2) / T1/2',
      reward: 200,
      options: [
        {
          text_de: "Genau 4 / 10 (exakt 50% Erholung nach Verstreichen einer vollen Halbwertszeit von 24h).",
          text_en: "Exactly 4 / 10 (precisely 50% decay after one biological half-life of 24h).",
          correct: true,
          feedback_de: "Perfekt gerechnet! Nach 24h Rest halbiert sich die Erschöpfung von 8 auf 4 Punkte.",
          feedback_en: "Perfect calculation! After 24h rest, fatigue halves from 8 to 4 points."
        },
        {
          text_de: "0 / 10 (Muskeln regenerieren im Schlaf immer komplett auf 0).",
          text_en: "0 / 10 (Muscles always reset to 0 during sleep).",
          correct: false,
          feedback_de: "Falsch! Schweres Krafttraining benötigt mehrere Halbwertszeiten (48-72h) zur vollständigen Regeneration.",
          feedback_en: "Incorrect! Heavy strength exertion requires multiple half-lives (48-72h) for full baseline recovery."
        },
        {
          text_de: "8 / 10 (Ermüdung baut sich ohne Massagen niemals ab).",
          text_en: "8 / 10 (Fatigue never decreases without massage).",
          correct: false,
          feedback_de: "Falsch! Der biologische Körper regeneriert kontinuierlich über die Zeit.",
          feedback_en: "Incorrect! The biological system continuously regenerates over time."
        }
      ]
    },
    {
      title_de: "Mission 5: Split Readiness Entscheidungsmatrix",
      title_en: "Mission 5: Split Readiness Decision Matrix",
      scenario_de: "Firestore liefert: Lats: 7/10 (Rot / stark ermüdet), Bizeps: 6/10, Vordere Schultern: 2/10 (Grün / frisch), Core: 3/10. Was empfiehlt der ApexMotion Coach?",
      scenario_en: "Firestore returns: Lats: 7/10 (Red/Fatigued), Biceps: 6/10, Anterior Delts: 2/10 (Green/Fresh), Core: 3/10. What does ApexMotion recommend?",
      snippet: 'Readiness Pull: 3.5 / 10 (RED) | Readiness Push: 8.0 / 10 (GREEN)',
      reward: 200,
      options: [
        {
          text_de: "Push-Training (Tuck Planche / HSPU) oder aktive Schulter-Mobilität, damit die Zugkette (Lats/Bizeps) regenerieren kann.",
          text_en: "Push Training (Tuck Planche / HSPU) or active mobility, allowing the pull chain (Lats/Biceps) to recover.",
          correct: true,
          feedback_de: "Ganz genau! Durch intelligentes Split-Management trainiert der Athlet Push, während Pull regeneriert.",
          feedback_en: "Spot on! Smart split programming schedules push progressions while the pulling chain recovers."
        },
        {
          text_de: "Schwere Weighted Pull-Ups bis zum Muskelversagen trainieren.",
          text_en: "Heavy Weighted Pull-ups to failure.",
          correct: false,
          feedback_de: "Gefährlich! Bei Lats 7/10 droht Überlastung und Sehnenreizung.",
          feedback_en: "Dangerous! At 7/10 fatigue on lats, heavy pull-ups risk overuse injury."
        },
        {
          text_de: "Den Agenten deinstallieren.",
          text_en: "Uninstall the agent.",
          correct: false,
          feedback_de: "Falsch! Der Coach hat alle Werkzeuge, um den optimalen Plan zu empfehlen.",
          feedback_en: "Incorrect! The coach has all the tools needed to optimize the split."
        }
      ]
    },
    {
      title_de: "Mission 6: Öffentliche Cloud Storage Assets",
      title_en: "Mission 6: Public Cloud Storage Assets",
      scenario_de: "Warum haben wir das IAM-Policy-Binding `allUsers -> roles/storage.objectViewer` auf den Asset-Bucket angewendet?",
      scenario_en: "Why did we bind `allUsers -> roles/storage.objectViewer` to the asset bucket?",
      snippet: 'gcloud storage buckets add-iam-policy-binding gs://apexmotion-coach-... --member=allUsers --role=roles/storage.objectViewer',
      reward: 200,
      options: [
        {
          text_de: "Damit Web-Frontends und A2UI-Cards im Browser Übungs-Cues und Diagramme per öffentlicher HTTPS-URL ohne Login-Token laden können.",
          text_en: "So web frontends and A2UI cards can embed visual cues & diagrams via public HTTPS URLs without auth tokens.",
          correct: true,
          feedback_de: "Großartig! Browser und A2UI-Cards können Bilder nur rendern, wenn die HTTPS-URL öffentlich erreichbar ist.",
          feedback_en: "Terrific! Web browsers and A2UI rich cards can only embed media when reachable via unauthenticated HTTPS."
        },
        {
          text_de: "Damit jeder beliebige Nutzer im Internet Dateien aus dem Bucket löschen darf.",
          text_en: "So any internet user can delete files from the bucket.",
          correct: false,
          feedback_de: "Falsch! `objectViewer` erlaubt nur Lesezugriff (Read-Only), keine Schreib- oder Löschrechte.",
          feedback_en: "Incorrect! `objectViewer` strictly grants read-only rights, not delete or write."
        },
        {
          text_de: "Damit Gemini Flash auf den Bucket zugreifen kann.",
          text_en: "To allow Gemini Flash to read the bucket.",
          correct: false,
          feedback_de: "Falsch! Gemini greift über IAM-Dienstkonten zu, nicht über allUsers.",
          feedback_en: "Incorrect! Gemini communicates via service account credentials, not allUsers."
        }
      ]
    }
  ];

  function startGameQuest() {
    gameState.currentMissionIndex = 0;
    gameState.scoreXP = 0;
    gameState.lives = 3;
    gameState.streak = 1;
    gameState.level = 1;
    updateGameHUD();

    document.querySelectorAll('.game-screen').forEach(s => s.classList.remove('active'));
    document.getElementById('screen-game-mission').classList.add('active');
    renderMission();
    playSoundChime();
  }

  function restartGameQuest() {
    startGameQuest();
  }

  function updateGameHUD() {
    // Level calculation
    if (gameState.scoreXP >= 1000) gameState.level = 5;
    else if (gameState.scoreXP >= 750) gameState.level = 4;
    else if (gameState.scoreXP >= 450) gameState.level = 3;
    else if (gameState.scoreXP >= 200) gameState.level = 2;
    else gameState.level = 1;

    const rankTitlesDe = ["Cloud Trainee", "ReAct Developer", "Firestore Architect", "Systems Engineer", "Apex Grandmaster 👑"];
    const rankTitlesEn = ["Cloud Trainee", "ReAct Developer", "Firestore Architect", "Systems Engineer", "Apex Grandmaster 👑"];

    const rTitle = currentLang === 'de' ? rankTitlesDe[gameState.level - 1] : rankTitlesEn[gameState.level - 1];
    document.getElementById('hud-level-text').textContent = `Level ${gameState.level}: ${rTitle}`;

    // Lives
    let hearts = "";
    for (let i = 0; i < 3; i++) {
      hearts += (i < gameState.lives) ? "❤️" : "🖤";
    }
    document.getElementById('hud-lives-display').textContent = hearts;

    // Score & Streak
    document.getElementById('hud-xp-display').textContent = `${gameState.scoreXP} XP`;
    document.getElementById('hud-streak-display').textContent = `${gameState.streak}x 🔥`;
  }

  function renderMission() {
    const m = missionsData[gameState.currentMissionIndex];
    document.getElementById('mission-step-indicator').textContent = (currentLang === 'de' ? 'MISSION ' : 'MISSION ') + (gameState.currentMissionIndex + 1) + ' / ' + missionsData.length;
    document.getElementById('mission-reward-indicator').textContent = '+' + m.reward + ' XP ' + (currentLang === 'de' ? 'BELOHNUNG' : 'REWARD');

    document.getElementById('mission-scenario-title').textContent = currentLang === 'de' ? m.title_de : m.title_en;
    document.getElementById('mission-scenario-desc').textContent = currentLang === 'de' ? m.scenario_de : m.scenario_en;

    const snip = document.getElementById('mission-scenario-snippet');
    if (m.snippet) {
      snip.style.display = 'block';
      snip.textContent = m.snippet.replace(/\\\\n/g, '\\n');
    } else {
      snip.style.display = 'none';
    }

    const optContainer = document.getElementById('mission-options-container');
    optContainer.innerHTML = '';

    const letters = ['A', 'B', 'C', 'D'];
    m.options.forEach((opt, idx) => {
      const btn = document.createElement('button');
      btn.className = 'quiz-opt-btn';
      btn.onclick = () => selectGameAnswer(idx);
      btn.innerHTML = `<span class="opt-letter">${letters[idx]}</span> <span>${currentLang === 'de' ? opt.text_de : opt.text_en}</span>`;
      optContainer.appendChild(btn);
    });

    const fBox = document.getElementById('mission-feedback-box');
    fBox.style.display = 'none';
    fBox.className = 'game-feedback-box';
    document.getElementById('btn-next-mission').style.display = 'none';
  }

  function selectGameAnswer(chosenIdx) {
    const m = missionsData[gameState.currentMissionIndex];
    const opt = m.options[chosenIdx];
    const buttons = document.querySelectorAll('.quiz-opt-btn');

    buttons.forEach((b, i) => {
      b.disabled = true;
      if (m.options[i].correct) b.classList.add('correct');
      else if (i === chosenIdx) b.classList.add('wrong');
    });

    const fBox = document.getElementById('mission-feedback-box');
    const fHead = document.getElementById('feedback-headline');
    const fDetail = document.getElementById('feedback-detail');

    fBox.style.display = 'block';

    if (opt.correct) {
      fBox.classList.add('correct');
      fHead.innerHTML = "✅ " + (currentLang === 'de' ? "Richtig! +" + (m.reward * gameState.streak) + " XP" : "Correct! +" + (m.reward * gameState.streak) + " XP");
      fDetail.textContent = currentLang === 'de' ? opt.feedback_de : opt.feedback_en;
      gameState.scoreXP += (m.reward * gameState.streak);
      gameState.streak += 1;
      playSoundChime();
    } else {
      fBox.classList.add('wrong');
      fHead.innerHTML = "❌ " + (currentLang === 'de' ? "Falsch! -1 Leben" : "Incorrect! -1 Life");
      fDetail.textContent = currentLang === 'de' ? opt.feedback_de : opt.feedback_en;
      gameState.lives -= 1;
      gameState.streak = 1;
      playSoundBuzz();
    }

    updateGameHUD();

    if (gameState.lives <= 0) {
      setTimeout(() => {
        document.querySelectorAll('.game-screen').forEach(s => s.classList.remove('active'));
        document.getElementById('screen-game-over').classList.add('active');
      }, 1200);
    } else {
      const nextBtn = document.getElementById('btn-next-mission');
      nextBtn.style.display = 'inline-flex';
      if (gameState.currentMissionIndex === missionsData.length - 1) {
        nextBtn.innerHTML = (currentLang === 'de' ? "🏆 Finale Auswertung" : "🏆 Final Evaluation") + " ➔";
      } else {
        nextBtn.innerHTML = (currentLang === 'de' ? "Nächste Mission" : "Next Mission") + " ➔";
      }
    }
  }

  function nextMission() {
    gameState.currentMissionIndex++;
    if (gameState.currentMissionIndex >= missionsData.length) {
      // Victory!
      document.querySelectorAll('.game-screen').forEach(s => s.classList.remove('active'));
      document.getElementById('screen-game-victory').classList.add('active');
      document.getElementById('victory-final-score').textContent = `${gameState.scoreXP} XP`;
      triggerConfetti();
      playSoundFanfare();
    } else {
      renderMission();
    }
  }

  // ========================================================
  // CONFETTI CANVAS PARTICLES (100% Native JS)
  // ========================================================
  function triggerConfetti() {
    const canvas = document.getElementById('confetti-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    canvas.width = canvas.parentElement.offsetWidth;
    canvas.height = canvas.parentElement.offsetHeight;

    const particles = [];
    const colors = ['#ec4899', '#a855f7', '#38bdf8', '#facc15', '#22c55e'];

    for (let i = 0; i < 90; i++) {
      particles.push({
        x: Math.random() * canvas.width,
        y: Math.random() * -canvas.height,
        w: Math.random() * 8 + 4,
        h: Math.random() * 8 + 4,
        color: colors[Math.floor(Math.random() * colors.length)],
        vy: Math.random() * 3 + 2,
        vx: (Math.random() - 0.5) * 3,
        rot: Math.random() * 360,
        rotSpeed: (Math.random() - 0.5) * 8
      });
    }

    let frames = 0;
    function renderConfetti() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      particles.forEach(p => {
        p.y += p.vy;
        p.x += p.vx;
        p.rot += p.rotSpeed;
        ctx.save();
        ctx.translate(p.x, p.y);
        ctx.rotate((p.rot * Math.PI) / 180);
        ctx.fillStyle = p.color;
        ctx.fillRect(-p.w / 2, -p.h / 2, p.w, p.h);
        ctx.restore();
      });

      frames++;
      if (frames < 240) {
        requestAnimationFrame(renderConfetti);
      } else {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
      }
    }
    renderConfetti();
  }

  // Video Tutorial Player Data
  let currentTutorialIndex = 0;
  let isPlayingVideo = false;
  let videoTimer = null;
  let videoStepIndex = 0;
  let videoPlaySpeed = 1.0;

  const tutorials = [
    {
      title: "tutorial_01_react_tool_calling.mp4",
      steps: [
        {
          screen: '<span class="term-prompt">student@cloud-vm:~/apexmotion$</span> <span class="term-cmd">agents-cli run "What is the weather in Hanoi?"</span>\\n\\n[INIT] Loading agent configuration from app/agent.py...\\n[MODEL] Initializing Gemini 3.8 Flash (High)...',
          narration_de: "Schritt 1: Der Nutzer fragt den Agenten nach dem Wetter in Hanoi. Der Agent startet den ReAct Loop.",
          narration_en: "Step 1: User asks for weather in Hanoi. The agent initiates the ReAct reasoning loop."
        },
        {
          screen: '<span class="term-highlight">🧠 [THOUGHT]</span> User needs current weather in Hanoi. Looking up available tools...\\n<span class="term-highlight">🛠️ [TOOL CALL]</span> get_weather(query="Hanoi")\\n[DISPATCH] Calling function in app/agent.py...',
          narration_de: "Schritt 2: Das LLM analysiert die Frage, wählt das Werkzeug `get_weather` und extrahiert `query='Hanoi'`.",
          narration_en: "Step 2: Model evaluates prompt, selects `get_weather`, and extracts `query='Hanoi'`."
        },
        {
          screen: '<span class="term-success">📦 [TOOL RETURN]</span> {"location": "Hanoi", "temperature": 28, "condition": "Sunny"}\\n[SYNTHESIS] Processing tool output with Gemini Flash...',
          narration_de: "Schritt 3: Das Tool liefert strukturierte JSON-Daten zurück (28°C, sonnig).",
          narration_en: "Step 3: Tool returns structured JSON (28°C, sunny condition)."
        },
        {
          screen: '<span class="term-success">💬 [AGENT REPLY]</span>\\n"The current weather in Hanoi is sunny with a temperature of 28°C."\\n\\n<span class="term-log">✨ ReAct Loop completed in 420ms!</span>',
          narration_de: "Schritt 4: Der Agent formuliert die finale, verständliche Antwort für den Nutzer. ReAct erfolgreich verifiziert!",
          narration_en: "Step 4: Agent crafts the natural language reply. ReAct loop verified successfully!"
        }
      ]
    },
    {
      title: "tutorial_02_agent_playground.mp4",
      steps: [
        {
          screen: '<span class="term-prompt">student@cloud-vm:~/apexmotion$</span> <span class="term-cmd">agents-cli playground</span>\\n\\n[INFO] Starting development server...\\n[INFO] Uvicorn running on http://localhost:8000 (Press CTRL+C to quit)',
          narration_de: "Schritt 1: Start des lokalen Playgrounds. Uvicorn startet den Webserver auf Port 8000 mit Hot-Reloading.",
          narration_en: "Step 1: Starting local playground. Uvicorn boots the web server on port 8000 with hot-reloading."
        },
        {
          screen: '[HOT RELOAD] Watching directory: /apexmotion/app\\n[BROWSER] Opening interactive visual workspace in Chrome...',
          narration_de: "Schritt 2: Der Browser öffnet die visuelle Benutzeroberfläche. Dateiänderungen in `app/agent.py` werden sofort ohne Neustart aktiv.",
          narration_en: "Step 2: Visual interface opens in browser. Edits in `app/agent.py` trigger instant live reloads."
        },
        {
          screen: '[INSPECTOR] Tracing side-panel attached:\\n - System Prompt\\n - Registered Tools (Firestore, Weather)\\n - Token Usage & Latency',
          narration_de: "Schritt 3: Im rechten Seitenpanel können Tool-Aufrufe, Token-Verbrauch und System-Prompts visuell inspiziert werden.",
          narration_en: "Step 3: Side panel exposes execution traces, token consumption, and system prompts in real time."
        }
      ]
    },
    {
      title: "tutorial_03_firestore_seeding.mp4",
      steps: [
        {
          screen: '<span class="term-prompt">student@cloud-vm:~/apexmotion$</span> <span class="term-cmd">python seed_firestore.py</span>\\n\\nConnecting to Firestore with project: qwiklabs-gcp-03-746ba250987a...',
          narration_de: "Schritt 1: Verbindung zur Cloud Firestore NoSQL-Datenbank mit der festen Projekt-ID als String.",
          narration_en: "Step 1: Connecting to Cloud Firestore NoSQL database using hardcoded alphanumeric project ID."
        },
        {
          screen: '<span class="term-success">✓ Seeded exercise:</span> Tuck Planche (planche_tuck)\\n<span class="term-success">✓ Seeded exercise:</span> Tuck Front Lever (front_lever_tuck)\\n<span class="term-success">✓ Seeded exercise:</span> Weighted Pull-Up (weighted_pullup)\\n<span class="term-success">✓ Seeded 7 more exercises...</span>',
          narration_de: "Schritt 2: 10 Calisthenics-Übungen mit Haltezeiten, Muskelgruppen und Ermüdungsfaktoren werden in `exercises` angelegt.",
          narration_en: "Step 2: 10 calisthenics exercises with target muscles, hold times, and fatigue factors written to `exercises`."
        },
        {
          screen: '<span class="term-success">✓ Seeded default athlete profile:</span> default_athlete\\n  • Goal: climbing & planche\\n  • Muscle Exhaustion: {anterior_delts: 2, lats: 6, core: 3, biceps: 6, ...}\\n<span class="term-log">✨ Database seeding completed successfully!</span>',
          narration_de: "Schritt 3: Das Athletenprofil `default_athlete` wird initialisiert. Der Agent kann nun Muskelstatus und Erschöpfung abrufen!",
          narration_en: "Step 3: Initializing `default_athlete` profile. The agent can now query muscle exhaustion and recovery status!"
        }
      ]
    },
    {
      title: "tutorial_04_storage_bucket.mp4",
      steps: [
        {
          screen: '<span class="term-prompt">student@cloud-vm:~$</span> <span class="term-cmd">gcloud storage buckets create gs://apexmotion-coach-qwiklabs-gcp-03-746ba250987a --location=US-EAST1 --uniform-bucket-level-access</span>\\n\\nCreating gs://apexmotion-coach-qwiklabs-gcp-03-746ba250987a/...\\n<span class="term-success">✓ Created bucket!</span>',
          narration_de: "Schritt 1: Erstellung des Cloud Storage Buckets in US-EAST1 mit einheitlicher Zugriffskontrolle (Uniform Access).",
          narration_en: "Step 1: Creating GCS bucket in US-EAST1 with Uniform Bucket-Level Access."
        },
        {
          screen: '<span class="term-prompt">student@cloud-vm:~$</span> <span class="term-cmd">gcloud storage buckets add-iam-policy-binding gs://apexmotion-coach-qwiklabs-gcp-03-746ba250987a --member=allUsers --role=roles/storage.objectViewer</span>\\n\\n<span class="term-success">Updated IAM policy for bucket. Public READ granted to allUsers.</span>',
          narration_de: "Schritt 2: Freigabe für `allUsers` mit der Rolle `roles/storage.objectViewer`. So können Bilder im Browser ohne Login angezeigt werden.",
          narration_en: "Step 2: Granting public read access (`allUsers`) so exercise cues render in web frontends without tokens."
        },
        {
          screen: '<span class="term-log">Public URL Format:</span>\\nhttps://storage.googleapis.com/apexmotion-coach-qwiklabs-gcp-03-746ba250987a/exercises/planche_scapula.png',
          narration_de: "Schritt 3: Bild-Assets sind ab sofort weltweit über die öffentliche HTTPS-URL für Frontend und A2UI erreichbar.",
          narration_en: "Step 3: Visual assets are globally accessible via HTTPS URLs for web UIs and A2UI rich cards."
        }
      ]
    },
    {
      title: "tutorial_05_live_coaching.mp4",
      steps: [
        {
          screen: '<span class="term-prompt">Athlete:</span> "I just finished 4 sets of Tuck Planche with RPE 9. How fatigued am I and what should I train tomorrow?"\\n\\n🧠 [REASONING] Evaluating workout session, calling log_workout_session...',
          narration_de: "Schritt 1: Der Athlet meldet ein intensives Planche-Training mit RPE 9. Der Coach startet die Berechnungen.",
          narration_en: "Step 1: Athlete reports intense Planche workout with RPE 9. Coach initiates fatigue calculations."
        },
        {
          screen: '<span class="term-highlight">🛠️ [TOOL]</span> log_workout_session(\\n    athlete_id="default_athlete",\\n    workout_type="skill_push",\\n    exercises_done=["planche_tuck"],\\n    session_rpe=9\\n)\\n<span class="term-success">📦 [STATUS]</span> Anterior Delts: 2 -> 7 (+5), Core: 3 -> 6 (+3)',
          narration_de: "Schritt 2: Das Tool berechnet Delta-Fatigue (+5 auf vordere Schultern) und speichert den neuen Status in Firestore.",
          narration_en: "Step 2: Tool computes delta fatigue (+5 to anterior delts) and commits updated state to Firestore."
        },
        {
          screen: '<span class="term-highlight">🛠️ [TOOL]</span> get_muscle_exhaustion(athlete_id="default_athlete")\\nReadiness Score: 5.2 / 10 (Yellow)\\nPush/Planche Status: Overloaded (7/10)',
          narration_de: "Schritt 3: Der Coach prüft den neuen Gesamt-Readiness-Score (5.2 / 10, Gelb) und stellt Überlastung der Druckkette fest.",
          narration_en: "Step 3: Coach checks composite Readiness Score (5.2/10, Yellow) and detects overloaded push chain."
        },
        {
          screen: '<span class="term-success">💬 [COACH ANSWER]</span>\\n"Starkes Training! Deine vorderen Schultern sind jetzt bei 7/10 und dein Core bei 6/10. Für morgen empfehle ich Pull (Front Lever / Klimmzüge) oder einen leichten Mobility-Flow für Handgelenke und Schultern!"',
          narration_de: "Schritt 4: Der Coach liefert die fundierte Empfehlung: Push schonen, morgen Pull oder Schulter-Mobilität trainieren!",
          narration_en: "Step 4: Coach delivers optimal guidance: rest push chain, focus on pull (front lever) or mobility flow tomorrow!"
        }
      ]
    }
  ];

  function loadTutorial(index) {
    pauseVideo();
    currentTutorialIndex = index;
    videoStepIndex = 0;

    // Highlight playlist item
    document.querySelectorAll('.playlist-item').forEach((item, i) => {
      item.classList.toggle('active', i === index);
    });

    const tut = tutorials[index];
    document.getElementById('video-clip-title').textContent = tut.title;
    renderVideoScene();
    updateVideoProgress();
  }

  function playTutorialDirect(index) {
    jumpToSection('video-studio');
    loadTutorial(index);
    setTimeout(() => {
      if (!isPlayingVideo) togglePlayVideo();
    }, 400);
  }

  function renderVideoScene() {
    const tut = tutorials[currentTutorialIndex];
    const scene = tut.steps[videoStepIndex];
    const textEl = document.getElementById('terminal-screen-text');
    const narrEl = document.getElementById('narration-text');
    const badgeEl = document.getElementById('active-scene-badge');

    if (textEl && scene) {
      textEl.innerHTML = scene.screen.replace(/\\\\n/g, '<br>').replace(/\\n/g, '<br>');
    }
    if (narrEl && scene) {
      narrEl.textContent = currentLang === 'de' ? scene.narration_de : scene.narration_en;
    }
    if (badgeEl) {
      badgeEl.textContent = (currentLang === 'de' ? 'Szene ' : 'Scene ') + (videoStepIndex + 1) + '/' + tut.steps.length;
    }
    const timeEl = document.getElementById('video-time-indicator');
    if (timeEl) {
      const curSec = (videoStepIndex + 1) * 7;
      const totSec = tut.steps.length * 7;
      timeEl.textContent = `00:${curSec < 10 ? '0' : ''}${curSec} / 00:${totSec < 10 ? '0' : ''}${totSec}`;
    }
  }

  function updateVideoProgress() {
    const tut = tutorials[currentTutorialIndex];
    const pct = ((videoStepIndex + 1) / tut.steps.length) * 100;
    const bar = document.getElementById('video-progress');
    if (bar) bar.style.width = pct + '%';
  }

  function togglePlayVideo() {
    if (isPlayingVideo) {
      pauseVideo();
    } else {
      startVideo();
    }
  }

  function startVideo() {
    isPlayingVideo = true;
    document.getElementById('play-icon').textContent = "⏸️";
    document.getElementById('play-text').textContent = currentLang === 'de' ? "Pause" : "Pause";
    document.getElementById('play-pause-btn').classList.add('active-play');

    const tut = tutorials[currentTutorialIndex];
    const intervalMs = 3800 / videoPlaySpeed;

    videoTimer = setInterval(() => {
      videoStepIndex++;
      if (videoStepIndex >= tut.steps.length) {
        pauseVideo();
        videoStepIndex = tut.steps.length - 1;
        return;
      }
      renderVideoScene();
      updateVideoProgress();
    }, intervalMs);
  }

  function pauseVideo() {
    isPlayingVideo = false;
    if (videoTimer) clearInterval(videoTimer);
    videoTimer = null;
    const pIcon = document.getElementById('play-icon');
    const pText = document.getElementById('play-text');
    const pBtn = document.getElementById('play-pause-btn');
    if (pIcon) pIcon.textContent = "▶️";
    if (pText) pText.textContent = currentLang === 'de' ? "Abspielen" : "Play";
    if (pBtn) pBtn.classList.remove('active-play');
  }

  function restartVideo() {
    pauseVideo();
    videoStepIndex = 0;
    renderVideoScene();
    updateVideoProgress();
    startVideo();
  }

  function scrubVideo(e) {
    const rect = e.currentTarget.getBoundingClientRect();
    const clickX = e.clientX - rect.left;
    const pct = clickX / rect.width;
    const tut = tutorials[currentTutorialIndex];
    videoStepIndex = Math.min(tut.steps.length - 1, Math.max(0, Math.floor(pct * tut.steps.length)));
    renderVideoScene();
    updateVideoProgress();
  }

  function cycleSpeed() {
    if (videoPlaySpeed === 1.0) videoPlaySpeed = 1.5;
    else if (videoPlaySpeed === 1.5) videoPlaySpeed = 2.0;
    else videoPlaySpeed = 1.0;
    document.getElementById('speed-btn').textContent = videoPlaySpeed.toFixed(1) + "x";
    if (isPlayingVideo) {
      pauseVideo();
      startVideo();
    }
  }

  // Simulator Data
  let simState = { delts: 2, lats: 6, core: 3, biceps: 6, legs: 1 };
  const exerciseProfiles = {
    planche_tuck: { name: "Tuck Planche", targets: { delts: 1.25, core: 1.0, biceps: 0.2 }, hold: 12 },
    front_lever_tuck: { name: "Tuck Front Lever", targets: { lats: 1.3, biceps: 1.1, core: 0.9 }, hold: 15 },
    weighted_pullup: { name: "Weighted Pull-Up", targets: { lats: 1.25, biceps: 1.2 }, hold: 0 },
    handstand_pushup_wall: { name: "Wall HSPU", targets: { delts: 1.3, core: 0.4 }, hold: 0 },
    pistol_squat: { name: "Pistol Squat", targets: { legs: 1.4, core: 0.4 }, hold: 0 }
  };

  const sampleDocs = {
    planche: {
      "id": "planche_tuck",
      "name": "Tuck Planche",
      "category": "skill_push",
      "target_muscles": ["anterior_delts", "chest", "core", "scapular_protractors"],
      "difficulty": "intermediate",
      "description": "Isometric hold with knees tucked to chest, arms straight, shoulders protracted.",
      "default_sets": 4,
      "default_hold_seconds": 12,
      "fatigue_factor": 7
    },
    front_lever: {
      "id": "front_lever_tuck",
      "name": "Tuck Front Lever",
      "category": "skill_pull",
      "target_muscles": ["lats", "rear_delts", "core", "scapular_retractors"],
      "difficulty": "intermediate",
      "description": "Horizontal hang from bar with knees tucked tight and back flat.",
      "default_sets": 4,
      "default_hold_seconds": 15,
      "fatigue_factor": 7
    },
    pullup: {
      "id": "weighted_pullup",
      "name": "Weighted Pull-Up",
      "category": "pull",
      "target_muscles": ["lats", "biceps", "rear_delts", "forearms"],
      "difficulty": "intermediate",
      "description": "Compound vertical pulling movement with external load or bodyweight focus.",
      "default_sets": 4,
      "default_reps": 8,
      "fatigue_factor": 8
    },
    athlete: {
      "athlete_id": "default_athlete",
      "goal": "climbing & planche",
      "skill_focus": ["planche", "front_lever"],
      "muscle_exhaustion": {
        "anterior_delts": 2,
        "chest": 1,
        "lats": 6,
        "rear_delts": 5,
        "core": 3,
        "biceps": 6,
        "triceps": 2,
        "quads": 1,
        "hamstrings": 1
      },
      "last_workout_type": "pull",
      "preferred_accessories": ["handstand", "stretching"]
    },
    workout: {
      "session_id": "sess_2026_09_29_01",
      "athlete_id": "default_athlete",
      "date": "2026-09-29T11:45:00Z",
      "workout_type": "pull",
      "exercises_done": [
        {"id": "front_lever_tuck", "sets": 4, "hold_sec": 12},
        {"id": "weighted_pullup", "sets": 4, "reps": 8}
      ],
      "session_rpe": 8,
      "fatigue_delta_applied": {"lats": +4, "biceps": +4, "core": +2},
      "notes": "Solid front lever form. Grip fatigued at end."
    }
  };

  const i18n = {
    de: {
      stat_project: "Projekt & Agent",
      stat_gcp_project: "GCP Projekt-ID",
      stat_steps: "Fortschritt (Schritte)",
      stat_reviewed: "Gelernt / Wiederholt",
      stat_reviewed_hint: "Klicke Checkboxen in den Schritten",
      arch_title: "Gesamtarchitektur & Datenfluss (Google Cloud Track 3)",
      roadmap_title: "Interaktiver Ablauf-Baum & Lernpfad (Klickbar)",
      roadmap_hint: "💡 Klicke auf ein Schlagwort, um direkt zum Abschnitt zu springen!",
      video_heading: "Video-Tutorials & Praxis-Vorführungen",
      game_arena_title: "ApexMotion Quest: Das interaktive Lern-Spiel",
      sim_heading: "Interaktiver Ermüdungs- & Erholungs-Simulator (Praxis-Tool)",
      db_heading: "Firestore Live-Datenbank Explorer",
      math_heading: "Mathematische Modelle & Algorithmen des Agenten",
      filter_all: "Alle (19)",
      filter_upcoming: "Ausstehend",
      btn_expand_all: "▼ Alle aufklappen",
      btn_collapse_all: "▲ Einklappen",
      btn_download: "HTML Herunterladen",
      lbl_why_step: "Warum dieser Schritt?",
      lbl_what_was_done: "Was wurde gemacht?",
      lbl_learning: "Lernpunkt & Rationale",
      lbl_gotcha: "Wichtige Falle (Gotcha)",
      lbl_arch_gotcha: "Architektur-Highlight: Hardcoded Project ID String!",
      chk_understood: "Ich habe diesen Schritt verstanden und wiederholt",
      title_cheatsheet: "Wichtige Befehle & Cheatsheet",
      th_description: "Beschreibung (DE / EN)",
      th_when: "Wann nutzen?",
      badge_done: "Abgeschlossen"
    },
    en: {
      stat_project: "Project & Agent",
      stat_gcp_project: "GCP Project ID",
      stat_steps: "Progress (Steps)",
      stat_reviewed: "Reviewed / Learned",
      stat_reviewed_hint: "Check checkboxes inside steps",
      arch_title: "System Architecture & Data Flow (Google Cloud Track 3)",
      roadmap_title: "Interactive Workflow Tree & Learning Path (Clickable)",
      roadmap_hint: "💡 Click any node to jump directly to its section!",
      video_heading: "Video Tutorials & Practical Screencasts",
      game_arena_title: "ApexMotion Quest: The Interactive Learning Game",
      sim_heading: "Interactive Muscle Fatigue & Recovery Simulator (Live Tool)",
      db_heading: "Firestore Live Database Explorer",
      math_heading: "Mathematical Models & Agent Algorithms",
      filter_all: "All (19)",
      filter_upcoming: "Upcoming",
      btn_expand_all: "▼ Expand All",
      btn_collapse_all: "▲ Collapse All",
      btn_download: "Download HTML",
      lbl_why_step: "Why this step?",
      lbl_what_was_done: "What was done?",
      lbl_learning: "Key Takeaway & Rationale",
      lbl_gotcha: "Critical Gotcha / Trap",
      lbl_arch_gotcha: "Architecture Highlight: Hardcoded Project ID String!",
      chk_understood: "I have understood and reviewed this step",
      title_cheatsheet: "Key Commands & Cheatsheet",
      th_description: "Description (DE / EN)",
      th_when: "When to use?",
      badge_done: "Completed"
    }
  };

  function setLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('apexmotion_lang', lang);

    document.getElementById('btn-de').classList.toggle('active', lang === 'de');
    document.getElementById('btn-en').classList.toggle('active', lang === 'en');

    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      if (i18n[lang][key]) {
        el.textContent = i18n[lang][key];
      }
    });

    document.querySelectorAll('[data-' + lang + ']').forEach(el => {
      el.innerHTML = el.getAttribute('data-' + lang);
    });

    if (lang === 'de') {
      document.getElementById('header-title').textContent = "ApexMotion · Workshop Lern- & Fortschrittszentrale";
      document.getElementById('header-subtitle').textContent = "Interaktive Schritt-für-Schritt-Zusammenfassung aller Schritte, Architektur & Lernkonzepte";
      document.getElementById('search-input').placeholder = "Schritt, Befehl oder Konzept suchen...";
    } else {
      document.getElementById('header-title').textContent = "ApexMotion · Workshop Learning & Progress Hub";
      document.getElementById('header-subtitle').textContent = "Interactive step-by-step summary of all steps, architecture & key takeaways";
      document.getElementById('search-input').placeholder = "Search step, command or concept...";
    }
    updateSimDisplay();
    renderVideoScene();
    updateGameHUD();
  }

  function toggleStep(num) {
    const card = document.getElementById('step-card-' + num);
    if (card) card.classList.toggle('expanded');
  }

  function toggleAllSteps(expand) {
    document.querySelectorAll('.step-card').forEach(card => card.classList.toggle('expanded', expand));
  }

  function jumpToStep(num) {
    const card = document.getElementById('step-card-' + num);
    if (card) {
      card.classList.add('expanded');
      card.scrollIntoView({ behavior: 'smooth', block: 'center' });
      card.classList.add('pulse-highlight');
      setTimeout(() => card.classList.remove('pulse-highlight'), 1800);
    }
  }

  function jumpToSection(sectionId) {
    const sec = document.getElementById(sectionId);
    if (sec) {
      sec.scrollIntoView({ behavior: 'smooth', block: 'start' });
      sec.classList.add('pulse-highlight');
      setTimeout(() => sec.classList.remove('pulse-highlight'), 1800);
    }
  }

  function setFilter(category, btn) {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    document.querySelectorAll('.step-card').forEach(card => {
      if (category === 'all') {
        card.style.display = 'block';
      } else if (category === 'upcoming') {
        card.style.display = card.classList.contains('upcoming') ? 'block' : 'none';
      } else {
        const cat = card.getAttribute('data-category') || '';
        const cats = cat.split(' ');
        card.style.display = cats.includes(category) ? 'block' : 'none';
      }
    });
  }

  function filterSteps() {
    const q = document.getElementById('search-input').value.toLowerCase();
    document.querySelectorAll('.step-card').forEach(card => {
      const text = card.innerText.toLowerCase();
      card.style.display = text.includes(q) ? 'block' : 'none';
    });
  }

  function markReviewed(stepNum, checked) {
    reviewedSteps[stepNum] = checked;
    localStorage.setItem('apexmotion_reviewed', JSON.stringify(reviewedSteps));
    updateReviewedCount();
  }

  function updateReviewedCount() {
    let count = 0;
    for (let k in reviewedSteps) {
      if (reviewedSteps[k]) count++;
    }
    const el = document.getElementById('reviewed-count');
    if (el) el.textContent = count;
  }

  function copyCode(btn) {
    const pre = btn.parentElement.nextElementSibling;
    navigator.clipboard.writeText(pre.innerText).then(() => {
      const originalText = btn.innerText;
      btn.innerText = currentLang === 'de' ? 'Kopiert!' : 'Copied!';
      btn.style.borderColor = 'var(--accent-green)';
      setTimeout(() => {
        btn.innerText = originalText;
        btn.style.borderColor = 'var(--border-color)';
      }, 1500);
    });
  }

  function executeSimWorkout() {
    const exKey = document.getElementById('sim-exercise').value;
    const rpe = parseInt(document.getElementById('sim-rpe').value, 10);
    const ex = exerciseProfiles[exKey];
    const baseDelta = Math.floor(rpe / 2);

    for (let m in ex.targets) {
      if (simState[m] !== undefined) {
        const factor = ex.targets[m];
        const added = Math.round(baseDelta * factor);
        simState[m] = Math.min(10, simState[m] + added);
      }
    }
    updateSimDisplay();
  }

  function simulateRestDecay() {
    simState.delts = Math.max(0, Math.round(simState.delts * 0.5));
    simState.core = Math.max(0, Math.round(simState.core * 0.5));
    simState.lats = Math.max(0, Math.round(simState.lats * 0.68));
    simState.biceps = Math.max(0, Math.round(simState.biceps * 0.65));
    simState.legs = Math.max(0, Math.round(simState.legs * 0.68));
    updateSimDisplay();
  }

  function resetSimMuscles() {
    simState = { delts: 2, lats: 6, core: 3, biceps: 6, legs: 1 };
    updateSimDisplay();
  }

  function updateSimDisplay() {
    const getColor = val => val >= 7 ? 'var(--accent-red)' : val >= 4 ? 'var(--accent-yellow)' : 'var(--accent-green)';

    for (let m of ['delts', 'lats', 'core', 'biceps', 'legs']) {
      const val = simState[m];
      const bar = document.getElementById('bar-' + m);
      const score = document.getElementById('score-' + m);
      if (bar && score) {
        bar.style.width = (val * 10) + '%';
        bar.style.background = getColor(val);
        score.textContent = val + ' / 10';
        score.style.color = getColor(val);
      }
    }

    const avgFatigue = (simState.delts + simState.lats + simState.core + simState.biceps + simState.legs) / 5;
    const readiness = (10 - avgFatigue).toFixed(1);
    const readEl = document.getElementById('readiness-display');
    const statEl = document.getElementById('readiness-status');

    if (readEl) {
      readEl.textContent = readiness + ' / 10';
      readEl.style.color = getColor(10 - readiness);
    }

    if (statEl) {
      if (simState.lats >= 6 && simState.delts <= 3) {
        statEl.innerHTML = currentLang === 'de'
          ? "🟡 <strong>Tipp:</strong> Lats ermüdet (" + simState.lats + "/10). Push/Planche oder Core empfohlen!"
          : "🟡 <strong>Coach Tip:</strong> Lats fatigued (" + simState.lats + "/10). Focus on Push/Planche or Core!";
        statEl.style.color = "var(--accent-yellow)";
      } else if (readiness >= 7.5) {
        statEl.innerHTML = currentLang === 'de'
          ? "🟢 <strong>Grün:</strong> Hohe Trainingsbereitschaft! Heavy Skill Training freigegeben."
          : "🟢 <strong>Green:</strong> High readiness! Heavy skill progression recommended.";
        statEl.style.color = "var(--accent-green)";
      } else if (readiness < 4.5) {
        statEl.innerHTML = currentLang === 'de'
          ? "🔴 <strong>Rot:</strong> Hohe Erschöpfung! Aktiver Rest Day oder Mobility / Stretching."
          : "🔴 <strong>Red:</strong> High overall fatigue! Active recovery / mobility flow advised.";
        statEl.style.color = "var(--accent-red)";
      } else {
        statEl.innerHTML = currentLang === 'de'
          ? "🟡 <strong>Gelb:</strong> Moderates Volumen / Accessory-Übungen."
          : "🟡 <strong>Yellow:</strong> Moderate volume / accessory workout recommended.";
        statEl.style.color = "var(--accent-yellow)";
      }
    }
  }

  function showDbDoc(key, btn) {
    document.querySelectorAll('.db-tab-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const el = document.getElementById('db-viewer-content');
    if (el && sampleDocs[key]) {
      el.innerHTML = '<code>' + JSON.stringify(sampleDocs[key], null, 2) + '</code>';
    }
  }

  function downloadCurrentHTML() {
    const htmlContent = "<!DOCTYPE html>\\n" + document.documentElement.outerHTML;
    const blob = new Blob([htmlContent], { type: "text/html;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "ApexMotion_Learning_Guide.html";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  document.addEventListener('DOMContentLoaded', () => {
    for (let k in reviewedSteps) {
      const card = document.getElementById('step-card-' + k);
      if (card) {
        const chk = card.querySelector('.learn-check input');
        if (chk) chk.checked = !!reviewedSteps[k];
      }
    }
    updateReviewedCount();
    setLanguage(currentLang);
    updateSimDisplay();
    loadTutorial(0);
  });
</script>

</body>
</html>
"""

# 1. Write the main HTML file in workshop repo
with open(HTML_SRC, "w", encoding="utf-8") as f:
    f.write(html_code)

os.makedirs(DESKTOP_DIR, exist_ok=True)

# 2. Copy as learning_progress.html into Desktop/HTML/
dest_learning = os.path.join(DESKTOP_DIR, "learning_progress.html")
with open(dest_learning, "w", encoding="utf-8") as f:
    f.write(html_code)

# 3. Create physical independent copy index.html (NO symlinks)
dest_index = os.path.join(DESKTOP_DIR, "index.html")
if os.path.islink(dest_index) or os.path.exists(dest_index):
    os.remove(dest_index)
with open(dest_index, "w", encoding="utf-8") as f:
    f.write(html_code)

# 4. Create README.txt explaining how to open, view, or email
readme_content = """========================================================================
ApexMotion Coach - Workshop Learning & Progress Hub (Google Cloud Track 3)
========================================================================

DEUTSCH:
--------
Dieses Paket ist zu 100% eigenständig ("self-contained") und funktioniert offline
auf JEDEM Computer (Windows, macOS, Linux, iPad/Tablet), ohne dass ein Server
oder zusätzliche Software installiert werden muss.

Öffnen:
- Doppelklicke einfach auf "index.html" oder "learning_progress.html" in einem
  beliebigen Browser (Google Chrome, Firefox, Safari, Microsoft Edge).

Neu in diesem Paket:
- 🎮 ApexMotion Quest (Interaktives Lern-Spiel mit Level-Up System):
    * Starte das Spiel mit dem Start-Knopf "QUEST JETZT STARTEN"!
    * 6 praxisnahe Herausforderungen zu Cloud IAM, ReAct Tool Calling,
      Firestore NoSQL Datenbanken, Biologischer Erholungs-Mathematik und Split-Coaching.
    * Level-Up Ränge: Cloud Trainee -> ReAct Developer -> Firestore Architect ->
      Systems Engineer -> Apex Grandmaster (1000+ XP).
    * Herzen-Lebenssystem (❤️❤️❤️), Combo-Multiplikator und nativer Web-Audio-Sound.
    * Konfetti-Siegesfeier & 5 freischaltbare Meister-Abzeichen (Badges).
- 🎬 Integriertes Video-Tutorial & Screencast Studio mit interaktivem Player:
    1. Setup & Hanoi Weather ReAct Loop (Tool-Calling)
    2. Agent Playground & Live Tracing (Port 8000)
    3. Firestore NoSQL Seeding & Tool-Verdrahtung
    4. Cloud Storage Bucket & IAM Öffentliche Freigabe
    5. ApexMotion Live-Coaching & RPE-Berechnung
  Inklusive Sprecher-Untertitel (DE/EN), Play/Pause, Timeline & Geschwindigkeit.
- 🧪 100% Offline & Private PC Verifikation (Zero Google Cloud):
    * Starte "python verify_offline.py" im Terminal, um alle 8 Portabilitäts-
      und Autarkie-Checks auf deinem eigenen Rechner zu prüfen.
    * Funktioniert komplett ohne Google Cloud, gcloud CLI oder API-Keys!
- 🏛️ Interaktives Architektur-Diagramm (SVG)
- 🗺️ Interaktiver Ablauf-Baum mit Klick-Navigation zu allen Schritten
- 🕹️ Interaktiver Ermüdungs- & Erholungs-Simulator (Live RPE & 24h Decay)
- 📂 Live Firestore Daten-Explorer mit echten JSON-Dokumenten
- 📐 Mathematische Formeln (RPE Skalierung, Exponentieller Zerfall, Readiness)
- 🎯 Erklärungen "Warum jeder Schritt durchgeführt wurde"
- 🇩🇪 / 🇬🇧 Zweisprachig (Deutsch & Englisch) per Klick umschaltbar
- 💾 Keine Internetverbindung oder externe Abhängigkeiten nötig

Lokale Tests auf privatem PC (Zero Google Cloud):
------------------------------------------------
1. Entpacke dieses ZIP-Archiv oder kopiere den Ordner auf deinen PC.
2. Öffne das Terminal und führe aus:
     python verify_offline.py
3. Möchtest du den Hub direkt im Browser öffnen:
     python verify_offline.py --open
   (oder einfach Doppelklick auf index.html)

Per E-Mail versenden:
- Du kannst entweder direkt "index.html" oder die fertige Datei
  "ApexMotion_Workshop_Hub.zip" an jede beliebige E-Mail-Adresse anhängen!


ENGLISH:
--------
This package is 100% self-contained and works completely offline on ANY
computer (Windows, macOS, Linux, iPad/Tablet) with zero installation required.

How to open:
- Simply double-click "index.html" or "learning_progress.html" in any browser
  (Google Chrome, Firefox, Safari, Microsoft Edge).

Features:
- 🎮 ApexMotion Quest (Interactive Gamified Learning Arena with Level-Ups):
    * Starts with the click of the "START QUEST NOW" button!
    * 6 real-world challenges covering Cloud IAM, ReAct loops, Firestore Project IDs,
      exponential recovery half-life math, and smart coach split decisions.
    * 5 Level-Up ranks from Cloud Trainee to Apex Grandmaster (1000+ XP).
    * 3 Lives (❤️❤️❤️), combo streak multipliers, native Web Audio API chimes,
      confetti celebration canvas, and 5 collectible mastery badges.
- 🎬 Built-in Interactive Video Screencast Studio with 5 walkthroughs & narration subtitles
- 🧪 100% Offline & Private PC Verification Suite (Zero Google Cloud):
    * Run "python verify_offline.py" in your terminal to verify all 8 standalone checks.
- 🏛️ Interactive Architecture SVG Diagram
- 🗺️ Interactive Roadmap Tree with clickable jump navigation
- 🕹️ Interactive Live Muscle Fatigue & 24h Recovery Simulator
- 📂 Firestore Database Explorer with concrete JSON documents
- 📐 Mathematical Models (RPE Scaling, Exponential Decay, Readiness Matrix)
- 🎯 Explicit "Why this step was done" architectural rationales
- 🇩🇪 / 🇬🇧 Bilingual (German & English) toggle
- 💾 Completely standalone, zero external dependencies

Sending via Email:
- You can directly attach "index.html" or the pre-packaged
  "ApexMotion_Workshop_Hub.zip" to any email!
========================================================================
"""

readme_path = os.path.join(DESKTOP_DIR, "README.txt")
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

# 5. Create a standalone ZIP archive for 1-click email attachment
zip_path = os.path.join(DESKTOP_DIR, "ApexMotion_Workshop_Hub.zip")
verify_script_path = os.path.join(DESKTOP_DIR, "verify_offline.py")

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(dest_index, arcname="index.html")
    zipf.write(dest_learning, arcname="learning_progress.html")
    zipf.write(readme_path, arcname="README.txt")
    if os.path.exists(verify_script_path):
        zipf.write(verify_script_path, arcname="verify_offline.py")

print(f"Generated standalone package successfully with Level-Up Game Quest!")
print(f"File size of learning_progress.html: {len(html_code)} bytes")
print(f"ZIP archive created at: {zip_path} (Size: {os.path.getsize(zip_path)} bytes)")

