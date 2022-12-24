import six
from google.protobuf import descriptor
from google.protobuf import text_encoding

from protocol.intellireader.contactless.poll_for_token_pb2 import PollingMode


def hex_format(message, indent=0, as_one_line=True):
    need_format = {
        'contactless.emv_tag.EmvTag': {
            'number': format_int,
            'value': format_str,
        },
        'contactless.token.Token': {
            'id': format_str,
            'answer_to_select': format_str,
            'atqa': format_str,
            'sak': format_str,
        },
        'contactless.transaction.PerformTransaction': {
            'transaction_date': format_str,
            'transaction_type': format_str,
            'terminal_country_code': format_str,
            'transaction_time': format_str,
            'transaction_currency_code': format_str,
            'merchant_category_code': format_str,
            'poll_for_token': format_subfield,
        },
        'contactless.transaction.TransactionResult': {
            'last_cmd': format_str,
            'last_sw_bytes': format_str,
            'emv_tags': format_list,
            'token': format_subfield,
            'encrypted_sensitive_data': format_str,
        },
        'contactless.transceive.BitArray': {
            'data': format_str,
        },
        'contactless.iso14443_4.Command': {
            'data': format_str,
        },
        'contactless.iso14443_4.Response': {
            'data': format_str,
        },
        'contactless.iso14443_4a.AnswerToSelect': {
            'data': format_str,
        },
        'contact.iso7816_4.TransmitApdu': {
            'command_apdu': format_str,
        },
        'contact.iso7816_4.ResponseApdu': {
            'body': format_str,
            'trailer': format_int,
        },
        'contact.emv_tag.EmvTag': {
            'number': format_int,
            'value': format_str,
        },
        'contact.transaction.PerformTransaction': {
            'transaction_date': format_str,
            'transaction_type': format_str,
            'terminal_country_code': format_str,
            'transaction_time': format_str,
            'transaction_currency_code': format_str,
            'merchant_category_code': format_str,
        },
        'contact.transaction.ContactTransactionResult': {
            'emv_tags': format_list,
            'online_pin_block': format_str,
        },
        'mifare.classic.auth.ClearKey': {
            'clear_key': format_str,
        },
        'mifare.classic.auth.SamKey': {
            'av2_args': format_subfield,
        },
        'mifare.plus.auth.ClearKey': {
            'clear_key': format_str,
            'key_type': format_subfield,
            'diversification_input': format_str,
        },
        'mifare.plus.auth.SamKey': {
            'key_type': format_subfield,
            'av2_args': format_subfield,
            'diversification_input': format_str,
        },
        'mifare.classic.read.Blocks': {
            'data': format_str,
        },
        'mifare.plus.read.Blocks': {
            'data': format_str,
        },
        'mifare.classic.write.WriteBlocks': {
            'data': format_str,
        },
        'mifare.plus.write.WriteBlocks': {
            'data': format_str,
        },
        'mifare.plus.key_type.KeyType': {
            'sector_key': format_subfield,
        },
        'mifare.plus.key_type.SectorKey': {
            'sector_number': format_default,
        },
        'mifare.av2.host_auth.AuthenticateHost': {
            'args': format_subfield,
            'key': format_str,
        },
        'mifare.av2.unlock.Unlock': {
            'args': format_subfield,
            'key': format_str,
        },
        'mifare.av2.args.AuthenticationArguments': {
            'slot': format_default,
        },
        'mifare.av2.change_keyentry.MifareKey': {
            'key': format_str,
        },
        'mifare.av2.change_keyentry.PlusKeyEntry': {
            'key': format_str,
        },
        'mifare.av2.change_keyentry.UltralightCKeyEntry': {
            'key': format_str,
        },
        'mifare.ultralight.read.Pages': {
            'data': format_str,
        },
        'mifare.ultralight.write.WritePages': {
            'data': format_str,
        },
        'mifare.ultralight.version.Version': {
            'raw_version_data': format_str,
        },
        'mifare.ultralight.password.ClearPassword': {
            'password': format_str,
        },
        'mifare.ultralight.password.PasswordAcknowledge': {
            'password_ack': format_str,
        },
        'mifare.generic.get_version.ProductVersionInfo': {
            'info': format_str,
        },
        'pinpad.online_pin.EnterOnlinePin': {
            'pan': format_str,
            'session_key': format_str,
        },
        'pinpad.online_pin.EntryResult': {
            'pin_block': format_str,
        },
        'srv.challenge.GetChallenge': {
            'data': format_str,
        },
        'srv.challenge.Challenge': {
            'data': format_str,
        },
        'srv.protection.Activate': {
            'encrypted_challenge': format_str,
        },
        'contactless.poll.PollForToken': {
            'timeout': format_default,
            'polling mode': PollingMode.LOW_POWER_POLLING

        },
        'stmcard.sri512.write.WriteBlocks': {
            'data': format_str,
        },
        'stmcard.sri512.read.Blocks': {
            'data': format_str,
        },
        'ntag.auth.ClearKey': {
            'clear_key': format_str,
        },
        'cipurse.sam.AuthorizeHwSam': {
            'aid': format_str,
            'password': format_str,
        },
        'cipurse.select.SelectFile': {
            'aid': format_str,
        },
        'cipurse.auth.EstablishSecureChannel': {
            'diversification_data': format_str,
        },
        'cipurse.read_binary.Binary': {
            'data': format_str,
        },
        'cipurse.update_binary.UpdateBinary': {
            'data': format_str,
        },
        'cipurse.read_record.Record': {
            'data': format_str,
        },
        'cipurse.update_record.UpdateRecord': {
            'data': format_str,
        },
        'cipurse.append_record.AppendRecord': {
            'data': format_str,
        },
        'qrcode.exchange.SendCommand': {
            'command': format_str,
        },
        'qrcode.exchange.ScannerReply': {
            'reply': format_str,
        },
        'troika.av3.read_ticket.Ticket': {
            'ticket_data': format_str,
        },
        'troika.av3.write_ticket.WriteTicket': {
            'sector': format_subfield,
            'ticket_params': format_str,
            'validate_params': format_str,
        },
        'troika.av3.write_ticket.WriteResult': {
            'sector_bitmap': format_str,
        },
    }
    formaters = need_format.get(message.DESCRIPTOR.full_name)
    if not formaters:
        return None
    result = []
    for field, value in message.ListFields():
        formater = formaters.get(field.name) or format_default
        result.append(formater(field, value))
    return ' '.join(result)


def format_str(field, value):
    return pair(field, '"{}"'.format(value.hex()))


def format_int(field, value):
    return pair(field, '{:X}'.format(value))


def format_subfield(field, value):
    return pair(field, subfield(value), ' ')


def format_list(field, value):
    items = []
    for element in value:
        items.append(format_subfield(field, element))
    return ' '.join(items)


def format_default(field, value):
    return pair(field, default_value(field, value))


def default_value(field, value):
    if field.cpp_type == descriptor.FieldDescriptor.CPPTYPE_ENUM:
        enum_value = field.enum_type.values_by_number.get(value, None)
        if enum_value is not None:
            return enum_value.name
        else:
            return str(value)
    elif field.cpp_type == descriptor.FieldDescriptor.CPPTYPE_STRING:
        out = '\"'
        if isinstance(value, six.text_type):
            out_value = value.encode('utf-8')
        else:
            out_value = value
        if field.type == descriptor.FieldDescriptor.TYPE_BYTES:
            out_as_utf8 = False
        else:
            out_as_utf8 = True
        out += text_encoding.CEscape(out_value, out_as_utf8)
        out += '\"'
        return out
    elif field.cpp_type == descriptor.FieldDescriptor.CPPTYPE_BOOL:
        if value:
            return 'true'
        else:
            return 'false'
    else:
        return str(value)


def subfield(field):
    return '{{ {} }}'.format(hex_format(field))


def pair(field, value, sep=': '):
    return '{}{}{}'.format(field.name, sep, value)
