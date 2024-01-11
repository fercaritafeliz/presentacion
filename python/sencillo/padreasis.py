vacaciones=False
diaDescanso=True

if vacaciones or diaDescanso:
    print('Puede asistir al juego')
else:
    print('tiene deberes por hacer')


if not (vacaciones or diaDescanso):
    print('tiene deberes por hacer')
else:
    print('Puede asistir al juego')