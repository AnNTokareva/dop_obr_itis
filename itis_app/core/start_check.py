from itis_app.core.model.lr_model import check_health


def start(age, cr_ph, ej_fr, platelets, time):
    data = [int(age), int(cr_ph), int(ej_fr), int(platelets), int(time)]

    d_e = check_health(data)

    return d_e
