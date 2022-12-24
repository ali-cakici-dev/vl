#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import serial
import os
import subprocess
import sys
import fcntl
import json
import constants
import paho.mqtt.client as mqtt
from time import sleep
# from models.mqtt.MakePay import MakePay
# Sil
import ctypes
import datetime

def catch_vendotek_vl(mdb_ser):
    try:
        constants.print_err_and_log_with_date('***** START VENDOTEK VL PROCESS *****')
        constants.readerCheckValue = datetime.datetime.now().replace(microsecond=0)
        client = mqtt.Client()
        client.message_callback_add('topic/reader/turnOn', reader_turnOn)
        client.message_callback_add('topic/reader/stateMachine', reader_stateMachine)
        client.message_callback_add('topic/reader/send/onlineCardData', reader_getOnlineCardData)
        client.message_callback_add('topic/reader/send/prePaidCardData', reader_getPrePaidCardData)

        client.connect('localhost', 1883, 60)

        client.on_connect = on_connect_vl
        # client.on_message = on_message_vl
        client.on_publish = on_publish_vl

        client.loop_start()
        # client.loop_forever()

        timeout = 6
        constants.card_detected = False
        constants.PROGRAM_STATUS['state'] = 2
        constants.print_err_and_log_with_date("Kart okutulması bekleniyor...")
        constants.displayIsInProcess = False
        constants.CCRPacketListenIsInProcess = False
        isCatchVendStarted_temp = False

        if constants.cardDetectedControl is True:
            sleep(0.1)
        constants.cardDetectedControl = False

        sleep(0.1)

        if constants.listen_vending_is_starting:
            constants.listen_vending_is_starting = False
        card_detected = False
        initial = datetime.datetime.now().replace(microsecond=0)
        initial_isCatchVendStarted = None
        constants.telemetryState = 1
        while True:
            # if constants.telemetryState is 1:
            #     publish_vl(client, 'topic/reader/getStateMachine', '', 1)
            #
            #     now = datetime.datetime.now().replace(microsecond=0)
            #     if (now - constants.readerCheckValue).seconds >= 10:
            #         print ('Okuyucu İletişim Hatası')
            #         return
            sleep(0.1)

            if constants.readerStatus is -1:
                constants.print_err_and_log_with_date('Waiting for VL Reader')
                sleep(0.1)
                continue
            elif constants.readerStatus is 0:
                constants.print_err_and_log_with_date('VL Reader was Open')
                sleep(0.1)
                continue
            elif constants.readerStatus is 3:
                if constants.stateMachine is 2 or constants.stateMachine is 4:
                    constants.print_err_and_log_with_date('CC okutuldu')

                    constants.sendDataVL = {
                        "command": 1,  # Set Screen
                        "screenNumber": 9,  # İŞLEMİNİZ YAPILIYOR,
                        "screenText": "İŞLEMİNİZ\n\nYAPILIYOR",
                        "screenTimeout": 0
                    }

                    json_data = json.dumps(constants.sendDataVL)
                    ret = publish_vl(client, 'topic/reader/onProcess', json_data, 2)
                    constants.sendDataVL = None

                    constants.readerStatus = 3
                    constants.stateMachine = 4
                    constants.isInProcess = True
                    constants.displayIsInProcess = False

                    constants.print_err_and_log_with_date("Card Info")
                    ccr = MakeCCRTransaction(user, ser, ccr_ser, automat_id, None)
                    ccr.start()  # Commit içi değişiklik

                    while constants.isInProcess:
                        constants.print_err_and_log_with_date('Wait finish for transaction!')
                        constants.print_err_and_log_with_date('constants.isInProcess: {}'.format(str(constants.isInProcess)))
                        if constants.sendDataVL is not None:
                            json_data = json.dumps(constants.sendDataVL)
                            ret = publish_vl(client, 'topic/reader/onProcess', json_data, 2)
                            constants.sendDataVL = None
                        time.sleep(0.01)
                        continue

                    # TODO: İşlem bitirilecek, Reader okuma moduna alınacak
                    publish_vl(client, 'topic/reader/setActive', '', 2)
                    constants.isInProcess = False
                    constants.readerStatus = 2
                    constants.stateMachine = 0
                    constants.telemetryState = 1
                    # If we do not set the current value after each operation, the processing time is 10 seconds
                    # will restart the software of the POS device because it will be large.
                    constants.readerCheckValue = datetime.datetime.now().replace(microsecond=0)
                    continue

            sleep(0.1)
    except Exception as e:
        constants.print_err_and_log_with_date("HATA - catch_vendotek_vl: {}".format(e))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        constants.print_err_and_log_with_date(exc_type, fname, exc_tb.tb_lineno)
        return


def on_publish_vl(client, userdata, result):
    try:
        constants.print_err_and_log_with_date("data published \n")
        pass
    except Exception as e:
        constants.print_err_and_log_with_date('Error - on_publish_vl: {}'.format(e))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        constants.print_err_and_log_with_date(exc_type, fname, exc_tb.tb_lineno)
        return None


def on_connect_vl(client, userdata, flags, rc):
    try:
        constants.print_err_and_log_with_date("Connected with result code " + str(rc))
        client.subscribe("topic/#", qos=2)
    except Exception as e:
        constants.print_err_and_log_with_date('Error - on_connect_vl: {}'.format(e))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        constants.print_err_and_log_with_date(exc_type, fname, exc_tb.tb_lineno)
        return None


def on_message_vl(client, userdata, msg):
    try:
        constants.print_err_and_log_with_date('on_message_vl')
        constants.print_err_and_log_with_date('Payload => {}'.format(str(msg.payload.decode())))
        if msg.payload.decode() == "Hello world!":
            constants.print_err_and_log_with_date("Yes! from test")
            # client.disconnect()
    except Exception as e:
        constants.print_err_and_log_with_date('Error - on_message_vl: {}'.format(e))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        constants.print_err_and_log_with_date(exc_type, fname, exc_tb.tb_lineno)
        return None


def publish_vl(client, topic, msg, qos=1):
    try:
        constants.print_err_and_log_with_date('publish_vl')
        constants.print_err_and_log_with_date('Client  => '.format(str(client)))
        constants.print_err_and_log_with_date('Topic   =>'.format(str(topic)))
        constants.print_err_and_log_with_date('Message =>'.format(str(msg)))
        # request = json.dumps(constans.prePaidProcessResult)
        response = client.publish(topic, msg, qos=qos)
        return response
    except Exception as e:
        constants.print_err_and_log_with_date('Error - publish: {}'.format(e))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        constants.print_err_and_log_with_date(exc_type, fname, exc_tb.tb_lineno)
        return None


def reader_turnOn(client, userdata, msg):
    try:
        constants.print_err_and_log_with_date('reader_turnOn')
        constants.readerStatus = 0

        constants.print_err_and_log_with_date('Payload => {}'.format(str(msg.payload.decode())))

        constants.print_err_and_log_with_date('Client => '.format(str(client)))
        constants.print_err_and_log_with_date('User Data =>'.format(str(userdata)))
        constants.print_err_and_log_with_date('MSG =>'.format(str(msg)))
        publish_vl(client, 'topic/reader/turnOnACK', '', 2)
    except Exception as e:
        constants.print_err_and_log_with_date('Error - reader_turnOn: {}'.format(e))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        constants.print_err_and_log_with_date(exc_type, fname, exc_tb.tb_lineno)
        return None


def reader_stateMachine(client, userdata, msg):
    try:
        constants.print_err_and_log_with_date('reader_stateMachine')
        constants.print_err_and_log_with_date('Payload => {}'.format(str(msg.payload.decode())))

        constants.print_err_and_log_with_date('Client => '.format(str(client)))
        constants.print_err_and_log_with_date('User Data =>'.format(str(userdata)))
        constants.print_err_and_log_with_date('MSG =>'.format(str(msg)))

        res = {}
        res = str(msg.payload.decode('utf-8', 'ignore'))
        res = json.loads(res)
        # print('Res => {}'.format(res))
        # print('Res readerStatus => {}'.format(res['readerStatus']))
        # print('Res readerStatus Type => {}'.format(type(res['readerStatus'])))
        # print('Res stateMachine => {}'.format(res['stateMachine']))
        # print('Res stateMachine Type => {}'.format(type(res['stateMachine'])))

        constants.readerStatus = int(res['readerStatus'])
        constants.stateMachine = int(res['stateMachine'])
        constants.readerCheckValue = datetime.datetime.now().replace(microsecond=0)

    except Exception as e:
        constants.print_err_and_log_with_date('Error - reader_stateMachine: {}'.format(e))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        constants.print_err_and_log_with_date(exc_type, fname, exc_tb.tb_lineno)
        return None


def reader_getOnlineCardData(client, userdata, msg):
    try:
        constants.print_err_and_log_with_date('reader_getOnlineCardData')
        constants.telemetryState = 0  # Now, do not send getStateMachine request
        constants.readerStatus = 3
        constants.stateMachine = 2
        constants.print_err_and_log_with_date('Payload => {}'.format(str(msg.payload.decode())))

        publish_vl(client, 'topic/reader/onlineCardDataACK', None)

    except Exception as e:
        constants.print_err_and_log_with_date('Error - reader_getOnlineCardData: {}'.format(e))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        constants.print_err_and_log_with_date(exc_type, fname, exc_tb.tb_lineno)
        return None


def reader_getPrePaidCardData(client, userdata, msg):
    try:
        constants.print_err_and_log_with_date('reader_getPrePaidCardData')
        constants.telemetryState = 0  # Now, do not send getStateMachine request
        constants.readerStatus = 3
        constants.stateMachine = 2
        constants.print_err_and_log_with_date('Payload => {}'.format(str(msg.payload.decode())))

        publish_vl(client, 'topic/reader/onlineCardDataACK', None)

    except Exception as e:
        constants.print_err_and_log_with_date('Error - reader_getPrePaidCardData: {}'.format(e))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        constants.print_err_and_log_with_date(exc_type, fname, exc_tb.tb_lineno)
        return None




if __name__ == "__main__":

    try:
        while True:

            while True:
                try:
                    test_client = mqtt.Client()
                    test_client.connect('localhost', 1883, 60)
                    time.sleep(0.2)
                    test_client.disconnect()
                    break
                except Exception as ex:
                    constants.otherInProcess = False
                    constants.print_err_and_log_with_date("\nMQTT Socket Hatası")
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    constants.print_err_and_log_with_date(exc_type, fname, exc_tb.tb_lineno)
                    os.system('chmod 777 /var/log/mosquitto/mosquitto.log')
                    time.sleep(0.1)
                    continue

            constants.print_err_and_log_with_date('Main script working - 2')
            currentyPath = os.getcwd()
            constants.print_err_and_log_with_date('CURRENT PATH >> ' + currentyPath)
            os.system('cd ' + currentyPath + '/vl && pm2 start ecosystem.json')
            # subprocess.call(["cd /evend/telemetry/vl && pm2 start ecosystem.json"], shell=False)
            catch_vendotek_vl("ser")

    except KeyboardInterrupt:
        # CCR.send_display_data(ccr_ser, None, display_timeout=0)
        # constants.print_err_and_log_with_date("Program kapatılıyor...")
        # CCR.send_display_show_logo(ccr_ser)
        exit()
