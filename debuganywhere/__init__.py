_wait_for_debugger_called = False


def wait_for_debugger(ngrok_auth_token, port=5678, silent=False):
    global _wait_for_debugger_called

    from pyngrok import ngrok
    import debugpy
    import sys

    if not _wait_for_debugger_called:
        debugpy.listen(port)
        ngrok.set_auth_token(ngrok_auth_token)
        tunnel = ngrok.connect(port, "tcp")
        if not silent:
          print(f"Debugger listening at: {tunnel.public_url}".strip(), file=sys.stderr, flush=True)
        _wait_for_debugger_called = True

    debugpy.wait_for_client()
    debugpy.breakpoint()
    return tunnel.public_url
