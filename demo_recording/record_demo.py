import asyncio
import os
import glob
from playwright.async_api import async_playwright

VIDEO_DIR = "/config/Desktop/BuildWithGemini/demo_recording/raw_video"
os.makedirs(VIDEO_DIR, exist_ok=True)

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )
        context = await browser.new_context(
            record_video_dir=VIDEO_DIR,
            record_video_size={"width": 1280, "height": 800},
            viewport={"width": 1280, "height": 800}
        )
        page = await context.new_page()

        print("Navigating to http://localhost:8080...")
        await page.goto("http://localhost:8080")
        await page.wait_for_timeout(2000)

        # 1. Showcase Theme switching
        print("Showcasing Theme Switching...")
        await page.select_option("#themeSelect", "outdoor")
        await page.wait_for_timeout(1500)
        await page.select_option("#themeSelect", "gym")
        await page.wait_for_timeout(1500)

        # 2. First Prompt: Core domain strength (Logging a workout session & computing fatigue decay)
        print("Running Prompt 1: Logging workout & fatigue decay...")
        prompt1 = "I just did 4 sets of weighted pull-ups and 3 sets of muscle-ups at RPE 8. Log this workout and check my muscle fatigue."
        await page.fill("#input", prompt1)
        await page.wait_for_timeout(1000)
        await page.click("button[type='submit']")

        # Wait for agent reply to arrive
        print("Waiting for Coach response...")
        # Wait until the placeholder "…" turns into actual reply content
        for _ in range(60):
            await page.wait_for_timeout(1000)
            bubbles = await page.query_selector_all(".dialogue-turn.agent .bubble")
            if len(bubbles) >= 2:
                last_bubble = bubbles[-1]
                text = await last_bubble.inner_text()
                if text != "…" and len(text) > 5:
                    print("Prompt 1 answered!")
                    break

        await page.wait_for_timeout(3000)

        # 3. Switch Celebrity Avatar
        print("Switching Coach to Master Lee...")
        await page.select_option("#coachSelect", "bruce")
        await page.wait_for_timeout(1500)

        # 4. Second, Richer Prompt: Visual Planche progression and biomechanical cues
        print("Running Prompt 2: Rich prompt with generated image / A2UI visual guide...")
        prompt2 = "What is the best way to train for the planche? Give me form cues, progressions, and show the visual posture."
        await page.fill("#input", prompt2)
        await page.wait_for_timeout(1000)
        await page.click("button[type='submit']")

        # Wait for second reply
        print("Waiting for visual card response...")
        for _ in range(60):
            await page.wait_for_timeout(1000)
            bubbles = await page.query_selector_all(".dialogue-turn.agent .bubble")
            if len(bubbles) >= 3:
                last_bubble = bubbles[-1]
                text = await last_bubble.inner_text()
                images = await last_bubble.query_selector_all("img")
                if text != "…" and (len(text) > 10 or len(images) > 0):
                    print("Prompt 2 answered!")
                    break

        # Let the viewer admire the card and comic layout
        await page.wait_for_timeout(5000)

        await context.close()
        await browser.close()
        print("Playwright recording completed!")

asyncio.run(run())
