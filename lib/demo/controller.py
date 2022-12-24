#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import datetime
import paho.mqtt.client as mqtt
import json
import sys

import common.failure_pb2 as failure_pb2
import intellireader.commands_pb2 as commands_pb2
import intellireader.contactless.transaction_pb2 as transaction_pb2
import intellireader.contactless.emv_removal_pb2 as emv_removal_pb2
import intellireader.contactless.poll_for_token_pb2 as poll_for_token_pb2
import intellireader.complex.poll_for_event_pb2 as poll_for_event_pb2
import intellireader.touchscreen.poll_touchscreen_pb2 as poll_touchscreen_pb2

import lib.proto
from protocol.intellireader.contactless.poll_for_token_pb2 import PollingMode
from . import screen, leds, buzz
from ..formatter import hex_format

from google.protobuf.text_format import *
from google.protobuf.message import *

from .contactless import *
from ..commands.gui import *
# import constans as constans


class DemoController:
    def __init__(self, proto, qrcode, gui):
        self.proto = proto
        self.qrcode = qrcode
        self.gui = gui
        self.readerStatus = 0  # 0 >Awaiting Connection, 1 >Ready, 2 >WaitCard, 3 >onProcess, 4 >onError
        self.turnOnACK = 0     # 0 > Wait ACK From v4G | 1 > Get ACK From v4G
        self.stateMachine = 0  # 0 >Idle, 1 >on Process, 2 >CC Read, 3 >Mifare Read, 4 >SendCCData, 5 >Cancel, 6 >Approved, 7 >Not Approved, 8 >Wait
        self.screenNumber = -1
        self.screenText = ""
        self.screenTimeout = 0
        self.s_counter = 0
        self.v_onlineCardDataACK = 0  # 0>None, 1>ACK

    def run(self):
        try:
            client = mqtt.Client()
            client.message_callback_add('topic/reader/turnOnACK', self.reader_turnOnACK)
            client.message_callback_add('topic/reader/getStateMachine', self.reader_getStateMachine)
            client.message_callback_add('topic/reader/onProcess', self.reader_onProcess)
            client.message_callback_add('topic/reader/setActive', self.reader_setActive)
            client.message_callback_add('topic/reader/setPassive', self.reader_setPassive)
            client.message_callback_add('topic/reader/screen/set', self.reader_screenSet)
            client.message_callback_add('topic/reader/screen/setApproved', self.reader_screenSetApproved)
            client.message_callback_add('topic/reader/screen/setCancel', self.reader_screenSetDeclined)
            client.message_callback_add('topic/reader/screen/setNotApproved', self.reader_screenSetNotApproved)
            client.message_callback_add('topic/reader/screen/setQR', self.reader_screenSetQR)
            client.message_callback_add('topic/reader/onlineCardDataACK', self.onlineCardDataACK)
            client.message_callback_add('topic/comm', self.on_comm)
            # client.message_callback_add('topic/receive', on_message_recieve)
            client.connect('localhost', 1883, 60)
            #
            client.on_connect = self.on_connect
            # client.on_message = self.on_message
            client.on_publish = self.on_publish

            client.loop_start()
            # # self.publish(client, 'topic/reader/turnOn', 'Hello from VL!', 0)

            # screen.awaiting(self.proto, None, 'İŞLEMİNİZ\n\nYAPILIYOR')
            # time.sleep(15)
            # show_screen_declined(self.proto, '', 'ISLEMINIZ\nONAYLANMADI')
            # time.sleep(15)

            # while True:
            #     self.publish(client, 'topic/reader/turnOn', 'Hello from VL!', 2)
            #     if self.turnOnACK is 0:
            #         print('Reader Wait Turn On Command From Telemetry')
            #         time.sleep(1)
            #         continue
            #     else:
            #         print('Send Turn On Command From Telemetry')
            #         self.readerStatus = 1
            #         time.sleep(0.2)
            #         break

            # show_all_screens(self.proto, '')

            # if self.gui:
            #     screen.tap_card(self.proto)

            # contactless_txn(self.proto, '')

            # leds.read_ok(self.proto)

            # screen.decline(self.proto, "112")
            # time.sleep(5)
            # screen.use_contact_iface(self.proto, "123")
            # time.sleep(5)
            #
            # screen.expired(self.proto, "123")
            # time.sleep(5)
            # screen.cdcvm_required(self.proto, "123")
            # time.sleep(5)
            self.readerStatus = 2
            while True:
                # screen.tap_card(self.proto)
                if self.readerStatus is 1:
                    print('Reader Wait For Telemetry')
                    screen.awaiting(self.proto, None, 'LÜTFEN BEKLEYİN')
                    time.sleep(0.5)
                    continue
                # ----------- ON PROCESS
                if self.readerStatus is 3:
                    if self.screenNumber is 0:
                        screen.tap_card(self.proto)
                    elif self.screenNumber is 5:
                        # İşleminiz onaylandı
                        show_screen_approved(self.proto)
                    elif self.screenNumber is 5:
                        # İşleminiz onaylanmadı
                        screen.decline(self.proto, None, 'ONAYLANMADI!'.encode('utf-8'))
                    elif self.screenNumber is 6:
                        # show_screen_wait(self.proto, '')
                        screen.awaiting(self.proto, None, 'ÜRÜN SEÇİNİZ')
                        time.sleep(5)
                    elif self.screenNumber is 7:
                        # show_screen_wait(self.proto, '')
                        screen.awaiting(self.proto, None, 'İŞLEMİNİZ\n\nYAPILIYOR')
                    elif self.screenNumber is 8:
                        # show_screen_wait(self.proto, '')
                        # TODO: Çarpı ikonu ile birlikte güncellenecek
                        # screen.awaiting(self.proto, None, 'SEÇİM YAPILMADI')
                        screen.decline(self.proto, None, 'SEÇİM\n\nYAPILMADI')
                    elif self.screenNumber is 9:
                        # show_screen_wait(self.proto, '')
                        screen.awaiting(self.proto, None, self.screenText)
                    elif self.screenNumber is 10:
                        # İşleminiz onaylanmadı
                        screen.decline(self.proto, None, self.screenText)
                    elif self.screenNumber is 11:
                        # İşleminiz onaylanmadı
                        screen.write_screen(self.proto, None, self.screenText)
                    elif self.screenNumber is 12:
                        # show_screen_wait(self.proto, '')
                        screen.write_screen(self.proto, None, self.screenText)
                    time.sleep(self.screenTimeout)
                    time.sleep(0.1)
                    continue
                elif self.readerStatus is 2:
                    # show_picture(self.proto,"luggage.bmp")
                    screen5()
                    # show_screen(self.proto, '')
                    # time.sleep(15)
                    # screen.tap_card_with_message(self.proto, 'KARTINIZI\n\nOKUTUNUZ')
                    self.s_counter += 1

                    event = self.polling()
                    if not self.gui:
                        continue

                    if event.HasField("contactless_txn_result"):
                        self.readerStatus = 3
                        result = event.contactless_txn_result
                        # screen.approve(self.proto, result)
                        # time.sleep(0.5)

                        """screen.transport_card(self.proto, result)
                        time.sleep(1)"""

                        if result and result.ByteSize() > 0:
                            self.stateMachine = 1
                            text = MessageToString(result, True, True, message_formatter=hex_format)

                            typeIndexFP = text.find("type: ") + 6
                            typeIndexLP = text.find("id: ") - 1
                            type = text[typeIndexFP:typeIndexLP]

                            print ('typeIndexFP: ' + str(typeIndexFP))
                            print ('typeIndexLP: ' + str(typeIndexLP))
                            print ('type: ' + str(type))

                            if type == "SMART_MX_WITH_MIFARE_1K" or type == "ISO_14443_4A":
                                self.stateMachine = 2
                                # screen.approve(self.proto, result)
                                # print ("SHOW SCREEN WAIT")
                                screen.write_screen(self.proto, result)
                                show_screen_wait(self.proto, None)
                                # time.sleep(10)

                                index1 = text.find("5A value: ") + 11
                                index2 = text.find("5F24 value: ") + 13
                                cardNumber = text[index1:index1+16]
                                cardExpDate = text[index2:index2+6]

                                print("Card Number >>> " + cardNumber)
                                print("Card Exp. Date >>> " + cardExpDate)

                                cardData = {
                                    'cardNumber': cardNumber,
                                    'expDate': cardExpDate
                                }

                                initial = datetime.datetime.now().replace(microsecond=0)
                                while True:
                                    self.publish(client, 'topic/reader/send/onlineCardData', json.dumps(cardData), 1)
                                    now = datetime.datetime.now().replace(microsecond=0)
                                    if (now - initial).seconds >= 5:
                                        print ("TIMEOUT")
                                        print ("V4G Kredi kartı bilgisini alamadı. ACK bilgisi göndermedi".encode('utf-8'))
                                        screen.decline(self.proto, None, 'ONAYLANMADI!'.encode('utf-8'))
                                        time.sleep(1.5)
                                        self.stateMachine = 0
                                        self.readerStatus = 2
                                        break
                                    if self.v_onlineCardDataACK is 1:
                                        self.readerStatus = 3  # onProcess
                                        # self.stateMachine = 4  # SendCCData
                                        self.stateMachine = 2
                                        # self.screenNumber = 6  # "İşleminiz Yapılıyor"
                                        break
                                    time.sleep(0.1)

                            elif type == "MIFARE_CLASSIC_1K":
                                screen.non_emv(self.proto, result)
                                time.sleep(1)
                                cardId = text[typeIndexLP+6:typeIndexLP+14]
                                print(cardId)
                                print("Card ID >>> " + cardId)
                                cardData = {
                                    'cardID': cardId
                                }

                                initial = datetime.datetime.now().replace(microsecond=0)
                                while True:
                                    self.publish(client, 'topic/reader/send/prePaidCardData', json.dumps(cardData), 1)
                                    now = datetime.datetime.now().replace(microsecond=0)
                                    if (now - initial).seconds >= 5:
                                        print ("TIMEOUT")
                                        print ("V4G Ön Ödemeli kartı bilgisini alamadı. ACK bilgisi göndermedi".encode('utf-8'))
                                        screen.decline(self.proto, None, 'ONAYLANMADI!'.encode('utf-8'))
                                        time.sleep(1.5)
                                        self.stateMachine = 0
                                        self.readerStatus = 2
                                        break
                                    if self.v_onlineCardDataACK is 1:
                                        self.readerStatus = 3  # onProcess
                                        # self.stateMachine = 4  # SendCCData
                                        self.stateMachine = 2
                                        # self.screenNumber = 6  # "İşleminiz Yapılıyor"
                                        break
                                    time.sleep(0.1)

                                self.readerStatus = 0

                            else:
                                screen.decline(self.proto, None, 'KART HATASI!'.encode('utf-8'))
                                self.stateMachine = 0
                                self.readerStatus = 2
                                print("Bu kart tipi desteklenmiyor.")
                                # TODO: Bu durum düşünülecek. Oguzhan kart.

                        ACTIONS[result.status](self.proto, result)

                    # if event.HasField("qrcode"):
                    #     screen.qrcode(self.proto, event.qrcode)

                    # if event.HasField("touchscreen_event"):
                    #     screen.ts_coordinates(self.proto, event.touchscreen_event)
        except Exception as e:
            print('Error - run: {}'.format(e))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return None

    def polling(self):
        event = poll_for_event_pb2.Event()
        self.emv_removal()

        while not self.wait_for_event(event):
            # if screen.last[1] != 'tap_card' and time.time() - screen.last[0] > 5:
                # if self.gui:
                #     screen.tap_card(self.proto)
            # time.sleep(10)
            if self.readerStatus is 0:
                break

        return event

    def wait_for_event(self, result):
        print("wait_for_event")
        request = commands_pb2.Complex()
        cmd = request.poll_for_event
        cmd.perform_txn.poll_for_token.timeout = 1000
        cmd.perform_txn.poll_for_token.polling_mode = PollingMode.LOW_POWER_POLLING
        cmd.perform_txn.poll_for_token.poll_stm_sri512 = True
        cmd.perform_txn.poll_for_token.poll_iso15693 = True
        cmd.perform_txn.poll_for_token.poll_ask_cts = True
        cmd.perform_txn.poll_for_token.light_up_led = True
        cmd.perform_txn.poll_for_token.enable_ecp = poll_for_token_pb2.RUSSIA_MOSCOW

        now = str(datetime.datetime.now())
        v_time = now.split(" ")
        date = v_time[0].split("-")
        clock = v_time[1].split(":")

        year, month, day = date[0], date[1], date[2]
        hour, minute, second= clock[0], clock[1], clock[2][0:2]

        # print(f"Today {day}.{month}.{year} - Time is {hour}:{minute}:{second}")

        cmd.perform_txn.amount_authorized = 100 # 1.00$
        cmd.perform_txn.transaction_date = b'\x13\x06\x13'
        cmd.perform_txn.transaction_time = b'\x12\x00\x00'
        cmd.perform_txn.transaction_type = b'\x00'
        cmd.perform_txn.terminal_country_code = b'\x06\x43'
        cmd.perform_txn.transaction_currency_code = b'\x06\x43'

        # if self.gui:
        cmd.poll_touchscreen.event_type = poll_touchscreen_pb2.COORDINATES

        # if self.qrcode:
        #     cmd.poll_for_qrcode.SetInParent()

        result = self.proto.exchange(request, result)

        # if not result and self.proto.last_error == failure_pb2.ABSENT_QRCODE_HARDWARE:
        #     self.qrcode = False

        return result

    def emv_removal(self):
        cmd = emv_removal_pb2.EmvRemoval()

        request = commands_pb2.ContactlessLevel1()
        request.emv_removal.SetInParent()

        return self.proto.exchange(request, None)

    def on_publish(self, client, userdata, result):
        print("data published \n")
        pass

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe("topic/#", qos=2)

    def on_message(self, client, userdata, msg):
        try:
            print('on_message')
            print('Payload => {}'.format(str(msg.payload.decode())))

            print('Client => '.format(str(client)))
            print('User Data =>'.format(str(userdata)))
            print('MSG =>'.format(str(msg)))

            comm_data = {}
            comm_data['message'] = str(msg.payload.decode('utf-8', 'ignore'))

            print('Comm Data Payload => {}'.format(comm_data))
            print('Comm Data message => {}'.format(comm_data['message']))

        except Exception as e:
            print('Error - on_message: {}'.format(e))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return None

    def publish(self, client, topic, msg, qos=1):
        try:
            print('Publish')
            # request = json.dumps(constans.prePaidProcessResult)
            response = client.publish(topic, msg, qos=qos)
            return response
        except Exception as e:
            print('Error - publish: {}'.format(e))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return None

    def on_comm(self, client, userdata, msg):
        print('on_comm')
        print('Payload => {}'.format(str(msg.payload.decode())))
        if msg.payload.decode() == "Hello world!":
            print("Yes! from Payment")

        print('Client => '.format(str(client)))
        print('User Data =>'.format(str(userdata)))
        print('MSG =>'.format(str(msg)))

        comm_data = {}
        comm_data['message'] = str(msg.payload.decode('utf-8', 'ignore'))

        print('Comm Data Payload => {}'.format(comm_data))

    def reader_turnOnACK(self, client, userdata, msg):
        try:
            print('reader_turnOnACK')
            self.turnOnACK = 1
            self.readerStatus = 2
            print('Reader Status > ', str(self.readerStatus))
            print('Payload => {}'.format(str(msg.payload.decode())))

            print('Client => '.format(str(client)))
            print('User Data =>'.format(str(userdata)))
            print('MSG =>'.format(str(msg)))
        except Exception as e:
            print('Error - reader_turnOnACK: {}'.format(e))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return None

    def reader_getStateMachine(self, client, userdata, msg):
        try:
            print('reader_getStateMachine')

            print('stateMachine => '.format(str(self.stateMachine)))
            print('readerStatus =>'.format(str(self.readerStatus)))
            now = datetime.datetime.now().replace(microsecond=0)
            data = {
                'stateMachine': self.stateMachine,
                'readerStatus': self.readerStatus,
                'now': str(now)
            }

            self.publish(client, 'topic/reader/stateMachine', json.dumps(data), 2)
        except Exception as e:
            print('Error - reader_getStateMachine: {}'.format(e))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return None

    def reader_onProcess(self, client, userdata, msg):
        try:
            print('reader_onProcess')

            print('Payload => {}'.format(str(msg.payload.decode())))

            print('Client => '.format(str(client)))
            print('User Data =>'.format(str(userdata)))
            print('MSG =>'.format(str(msg)))

            res = {}
            res = str(msg.payload.decode('utf-8', 'ignore'))
            res = json.loads(res)
            # print('MSG Data => {}'.format(res))
            # print('Res readerStatus => {}'.format(res['readerStatus']))
            # print('Res readerStatus Type => {}'.format(type(res['readerStatus'])))
            # print('Res stateMachine => {}'.format(res['stateMachine']))
            # print('Res stateMachine Type => {}'.format(type(res['stateMachine'])))

            command = int(res['command'])

            if command is 1:
                # Set Screen Command Handler
                print('Set Screen Number => {}'.format(res['screenNumber']))
                print('Set Screen Text => {}'.format(res['screenText'].encode()))
                print('Set Screen Timeout => {}'.format(res['screenTimeout']))
                self.screenNumber = int(res['screenNumber'])
                self.screenTimeout = res['screenTimeout']
                screenText = res['screenText']
                if screenText is not None:
                    self.screenText = screenText
        except Exception as e:
            print('Error - reader_onProcess: {}'.format(e))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return None

    def reader_setActive(self, client, userdata, msg):
        try:
            print('reader_setActive')
            self.readerStatus = 2
            self.stateMachine = 0
            self.screenNumber = -1
            self.screenText = ""
            self.screenTimeout = 0

            print('Reader Status > ', str(self.readerStatus))
            print('State Machine  > ', str(self.stateMachine))
            print('Payload => {}'.format(str(msg.payload.decode())))

            print('Client => '.format(str(client)))
            print('User Data =>'.format(str(userdata)))
            print('MSG =>'.format(str(msg)))
        except Exception as e:
            print('Error - reader_setActive: {}'.format(e))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return None

    def reader_setPassive(self, client, userdata, msg):
        try:
            print('reader_setPassive')
            self.readerStatus = 0
            print('Reader Status > ', str(self.readerStatus))
            print('Payload => {}'.format(str(msg.payload.decode())))

            print('Client => '.format(str(client)))
            print('User Data =>'.format(str(userdata)))
            print('MSG =>'.format(str(msg)))
        except Exception as e:
            print('Error - reader_setPassive: {}'.format(e))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return None

    def reader_screenSetQR(self, client, userdata, msg):
        try:
            print('reader_screenSetQR')
            print('Payload => {}'.format(str(msg.payload.decode())))

            print('Client => '.format(str(client)))
            print('User Data =>'.format(str(userdata)))
            print('MSG =>'.format(str(msg)))
        except Exception as e:
            print('Error - reader_onProcess: {}'.format(e))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return None

    def reader_screenSetApproved(self, client, userdata, msg):
        try:
            print('reader_screenSetApproved')
            print('Payload => {}'.format(str(msg.payload.decode())))

            print('Client => '.format(str(client)))
            print('User Data =>'.format(str(userdata)))
            print('MSG =>'.format(str(msg)))

            show_screen_approved(self.proto, '')
            time.sleep(1.5)
        except Exception as e:
            print('Error - reader_screenSetApproved: {}'.format(e))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return None

    def reader_screenSet(self, client, userdata, msg):
        try:
            print('reader_screenSet')
            print('Payload => {}'.format(str(msg.payload.decode())))

            res = {}
            res = str(msg.payload.decode('utf-8', 'ignore'))
            res = json.loads(res)
            # print('Res => {}'.format(res))
            # print('Res readerStatus => {}'.format(res['readerStatus']))
            # print('Res readerStatus Type => {}'.format(type(res['readerStatus'])))
            # print('Res stateMachine => {}'.format(res['stateMachine']))
            # print('Res stateMachine Type => {}'.format(type(res['stateMachine'])))

            self.screenNumber = int(res['screenNumber'])

            print('Client => '.format(str(client)))
            print('User Data =>'.format(str(userdata)))
            print('MSG =>'.format(str(msg)))
        except Exception as e:
            print('Error - reader_screenSet: {}'.format(e))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return None


    def reader_screenSetDeclined(self, client, userdata, msg):
        try:
            print('reader_screenSetDeclined')
            print('Payload => {}'.format(str(msg.payload.decode())))

            print('Client => '.format(str(client)))
            print('User Data =>'.format(str(userdata)))
            print('MSG =>'.format(str(msg)))

            screen.decline(self.proto, None, 'KARTINIZDA ODEME \n\n ALINAMADI'.encode('utf-8'))
            time.sleep(3)
        except Exception as e:
            print('Error - reader_screenSetDeclined: {}'.format(e))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return None

    def reader_screenSetNotApproved(self, client, userdata, msg):
        try:
            print('reader_screenSetNotApproved')
            print('Payload => {}'.format(str(msg.payload.decode())))

            print('Client => '.format(str(client)))
            print('User Data =>'.format(str(userdata)))
            print('MSG =>'.format(str(msg)))

            screen.decline(self.proto, None, 'KARTINIZDA ODEME \n\n ALINAMADI'.encode('utf-8'))
            time.sleep(5)
        except Exception as e:
            print('Error - reader_screenSetNotApproved: {}'.format(e))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return None

    def onlineCardDataACK(self, client, userdata, msg):
        try:
            print('onlineCardDataACK')
            print('Payload => {}'.format(str(msg.payload.decode())))
            self.v_onlineCardDataACK = 1
            print('Client => '.format(str(client)))
            print('User Data =>'.format(str(userdata)))
            print('MSG =>'.format(str(msg)))
        except Exception as e:
            print('Error - onlineCardDataACK: {}'.format(e))
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return None


ACTIONS = {
    transaction_pb2.ONLINE_AUTHORIZATION_REQUIRED: screen.approve,
    transaction_pb2.OFFLINE_APPROVED: screen.approve,
    transaction_pb2.OFFLINE_DECLINED: screen.decline,
    transaction_pb2.USE_CONTACT_INTERFACE: screen.use_contact_iface,
    transaction_pb2.UNABLE_PERFORM_TRANSACTION: screen.decline,
    transaction_pb2.NON_EMV_CARD: screen.non_emv,
    transaction_pb2.CARD_EXPIRED: screen.expired,
    transaction_pb2.AUTHORIZATION_ON_CARDHOLDER_DEVICE_REQUIRED: screen.cdcvm_required,
}