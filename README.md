<div align="center">

# 🔗 URL Shortener — `fwd.mj46.in`

A fast, lightweight, zero-dependency client-side URL shortener interface and analytics viewer hosted on **GitHub Pages**, backed by a custom backend API.

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](#)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](#)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](#)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-222222?style=for-the-badge&logo=github&logoColor=white)](#)

</div>

---

## ✨ Features

- ⚡ **Instant URL Shortening** — Condense long URLs into clean, shareable short codes.
- 📊 **Built-in Link Analytics** — Append `+` to any short URL (e.g., `fwd.mj46.in/xyz+`) to view click metrics, creation dates, and access history.
- 🔀 **Client-Side SPA Routing** — Leverages a custom GitHub Pages `404.html` handler to perform dynamic routing and client-side redirects.
- 💾 **Local Link History** — Keeps a local log of up to 25 generated links in browser storage (`localStorage`) for quick copying and reference.
- 🌓 **Dark & Light Mode** — Theme switcher auto-detects system preferences and persists user choices.
- 📱 **Fully Responsive Glassmorphic UI** — Modern interface crafted with pure CSS variables and smooth transitions.

---

## 🚀 How It Works

### 1. Shortening a URL
1. Paste your target link into the input field.
2. Click **Shorten URL** to send a payload to `https://api.mj46.in/api/v1/url-shortener/`.
3. Copy the returned short URL directly to your clipboard.

---

### 2. Redirection & Analytics via GitHub Pages Routing
Since static site hosts like GitHub Pages do not support server-side routing for dynamic paths (e.g., `/xyz`), this application uses `404.html` as a fallback router:

| Path | Behavior |
| :--- | :--- |
| **`/`** | Serves the main generator web app (`index.html`). |
| **`/{code}`** | Intercepted by `404.html` -> Fetches target URL from API -> Performs instant redirect via `window.location.replace`. |
| **`/{code}+`** | Intercepted by `404.html` -> Fetches metadata from API -> Renders the **Link Analytics** dashboard. |

---

## 🛠️ Tech Stack

* **Frontend:** Vanilla HTML5, CSS3 (CSS Custom Properties & Flexbox/Grid), JavaScript (ES6+ Fetch API)
* **Router:** SPA routing layer via custom GitHub Pages `404.html` fallback engine
* **API Backend:** `https://api.mj46.in/api/v1/url-shortener/`
* **Storage:** Client-side `localStorage`

---

## 👨‍💻 Author

**Abin Santhosh (MJTech46)**

* 🌐 **Website:** [mj46.in](https://www.mj46.in)
* 🛠️ **Tools Hub:** [tools.mj46.in](https://tools.mj46.in)
* 🐙 **GitHub:** [@MJTech46](https://github.com/MJTech46)