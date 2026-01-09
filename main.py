import sys
import os
import threading
import time
import urllib.request
import webview

FLASK_URL = "http://127.0.0.1:5000"

LOADING_HTML = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            background-color: #1a1a1a;
            color: #ffffff;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .loader { text-align: center; }
        @-webkit-keyframes spin {
            from { -webkit-transform: rotate(0deg); }
            to { -webkit-transform: rotate(360deg); }
        }
        @keyframes spin {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
        .spinner {
            width: 40px;
            height: 40px;
            border: 3px solid #333;
            border-top-color: #fff;
            border-radius: 50%;
            -webkit-animation: spin 1s linear infinite;
            animation: spin 1s linear infinite;
            margin: 0 auto 16px;
        }
    </style>
</head>
<body>
    <div class="loader">
        <div class="spinner"></div>
        <div>Loading...</div>
    </div>
</body>
</html>
"""


def get_base_dir():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))


def start_flask():
    from app import app, app_startup_tasks
    app_startup_tasks()
    app.run(debug=False, use_reloader=False, threaded=True)


def wait_for_flask_and_load(window, timeout=30):
    """Wait for Flask server to be ready, then load the URL."""
    start = time.time()
    while time.time() - start < timeout:
        try:
            urllib.request.urlopen(FLASK_URL, timeout=1)
            window.load_url(FLASK_URL)
            return
        except Exception:
            time.sleep(0.1)


def on_loaded(window):
    """Called when loading screen DOM is ready."""
    # Unsubscribe immediately to prevent being called again when Flask page loads
    window.events.loaded -= on_loaded
    # Start polling Flask in a separate thread
    threading.Thread(target=wait_for_flask_and_load, args=(window,), daemon=True).start()


if __name__ == "__main__":
    # Start Flask in background thread
    flask_thread = threading.Thread(target=start_flask, daemon=True)
    flask_thread.start()

    # Create window with dark background color (shown before WebView loads)
    # and loading HTML (shown once WebView initializes)
    window = webview.create_window(
        title="OP-Z Sample Manager",
        html=LOADING_HTML,
        width=1280,
        height=720,
        background_color="#1a1a1a",  # Matches loading screen - no white flash
    )

    # Wait for loading screen DOM to be ready, then start polling Flask
    window.events.loaded += on_loaded

    # Start the webview (blocks until window is closed)
    webview.start()
