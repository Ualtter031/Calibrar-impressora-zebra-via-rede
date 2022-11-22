import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

svc = """
! U1 setvar "media.type" "label"
! U1 setvar "media.sense_mode" "gap"
! U1 setvar "ezpl.head_close_action" "feed"
! U1 setvar "ezpl.power_up_action" "calibrate"
! U1 setvar "ezpl.label_length_max" "2"
! U1 setvar "device.command_override.add" "^MN"
! U1 setvar "device.command_override.add" "^LL"
! U1 setvar "ezpl.print_mode" "tear off"
! U1 setvar "zpl.left_position" "-90"
! U1 setvar "zpl.label_top" "8"

! U1 getvar "media.type" "label"
! U1 getvar "media.sense_mode" "gap"
! U1 getvar "ezpl.head_close_action" "feed"
! U1 getvar "ezpl.power_up_action" "calibrate"
! U1 getvar "ezpl.label_length_max" "2"
! U1 getvar "device.command_override.add" "^MN"
! U1 getvar "device.command_override.add" "^LL"
! U1 getvar "ezpl.print_mode" "tear off"
! U1 getvar "zpl.left_position" "-90"
! U1 getvar "zpl.label_top" "8"
"""
xd = """
! U1 setvar "media.type" "label"
! U1 setvar "media.sense_mode" "gap"
! U1 setvar "ezpl.head_close_action" "feed"
! U1 setvar "ezpl.power_up_action" "calibrate"
! U1 setvar "ezpl.label_length_max" "2"
! U1 setvar "device.command_override.add" "^MN"
! U1 setvar "device.command_override.add" "^LL"
! U1 setvar "ezpl.print_mode" "tear off"
! U1 setvar "zpl.left_position" "100"
! U1 setvar "zpl.label_top" "100"

! U1 getvar "media.type" "label"
! U1 getvar "media.sense_mode" "gap"
! U1 getvar "ezpl.head_close_action" "feed"
! U1 getvar "ezpl.power_up_action" "calibrate"
! U1 getvar "ezpl.label_length_max" "2"
! U1 getvar "device.command_override.add" "^MN"
! U1 getvar "device.command_override.add" "^LL"
! U1 getvar "ezpl.print_mode" "tear off"
! U1 getvar "zpl.left_position" "100"
! U1 getvar "zpl.label_top" "100"
    """

ip = str(input ("Informe o ip do dispositivo: "))
client.connect((ip,6101))
print('Conectando !\n')

operacao_imp = input(f'Qual operação a impressora pertence, XD ou SVC? ').encode('utf-8')

if  operacao_imp == svc:
    print(svc)
else:
    print (xd)

client.send(operacao_imp)

print(operacao_imp,'foi selecionado com sucesso, aguarde 3 minutos e reinicie o dispositivo!')
