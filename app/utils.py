def message(status, message):
    response_object = {"status": status, "message": message}
    return response_object


def validation_error(status, errors):
    response_object = {"status": status, "errors": errors}

    return response_object

# Removido o code
def err_resp(msg, reason):
    err = message(False, msg)
    err["error_reason"] = reason
    return err


def internal_err_resp():
    err = message(False, "Algo deu errado durante o processo!")
    err["error_reason"] = "server_error"
    return err, 500
