# Enhancing Smart Home Automation with Gesture-Controlled Contactless Switch 💡

🤖✨ Hand Gesture Light Control
"Wave Your Hand, Command the Light!" 💡👋

🚀 Project Overview:
This project demonstrates a contactless smart light control system using hand gesture recognition and an ESP32 microcontroller. The system detects specific hand gestures through a webcam feed using OpenCV and cvzone, and sends serial commands to the ESP32 to switch the light ON or OFF.

This smart system uses:

👁️ Computer Vision (OpenCV + MediaPipe) to track your hand gestures.

⚡ ESP32 to execute commands instantly.

🔌 Zero Physical Contact – perfect for hygiene & futuristic homes!

---

# 🛠️ Tech Stack

Layer	Tech Used	Role:

|  LAYER     | TECH USED                   | ROLE                                |
|--------:   |----------------------------|-------------------------------------|
| Vision 👀  | Python + OpenCV + cvzone| Detects 👆✌️ gestures in real-time   |
|  Brain 🧠  | ESP32 (Arduino C++)	   |  Processes commands & controls LED  |
|   Comms 📡 | Serial (UART)	         |  Bridges PC ↔ ESP32 wirelessly      |

---

# 🎮 Gesture Mapping

| Gesture | Fingers Detected | Action |
|--------:|------------------|--------|
|   ☝️    | Index finger (1)  | Light 💡 → ON |
|   ✌️    | Index + Middle (2)| Light 💡 → OFF |

---


# 🚀 Key Python Features:

📸 Real-Time Webcam Feed (60 FPS)

🖐️ Robust Hand Tracking (Works in low light!)

⚡ Low Latency (< 0.5s response time)

🛜 Works fully offline (no Wi-Fi required)

✅ Reliable, low-latency control

---


# 🌟 Why This Rocks?

✅ No Wi-Fi Needed – Works 100% offline!

✅ Plug-and-Play – Set up in < 5 mins.

✅ Scalable – Add more gestures (e.g., fan speed 🌪️).

---

# 🖥️ Python Side (Gesture Detection)

📦 Install Dependencies:

```
pip install opencv-python mediapipe cvzone numpy --upgrade
```

### 🔗 Required Libraries

Install these libraries using pip:
```
pip install opencv-python mediapipe cvzone
```

---



# 🔥 Bonus Ideas

📱 Add Mobile Alerts (Twilio SMS when light turns on)

🌐 IoT Integration (Control via Telegram Bot 🤖)

🎚️ Dimming Support (Use thumb gestures for brightness!)

## 👨‍💻 Ready to Build?
Clone the repo & light up your room WITHOUT TOUCHING A SWITCH! 🎉

