import uvicorn, os
PORT = int(os.getenv("PORT", "8000"))
uvicorn.run(app, host="0.0.0.0", port=PORT)
