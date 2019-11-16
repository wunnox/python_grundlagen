# smidi.py: A simple midi-file library
# make a single file version for midi-outfile only.
# Original code is from Max M's site here (GPL)
# http://www.mxm.dk/products/public/pythonmidi

"""
include source codes from
- constants.py
- DataTypeConverters.py
- RawOutstreamFile.py
- MidiOutStream.py
- MidiOutFile.py
"""

from struct import pack, unpack
from types import StringType
from cStringIO import StringIO


#=================== constants.py ===================================#
###################################################
# Definitions of the different midi events


###################################################
# Midi channel events (The most usual events)
# also called "Channel Voice Messages"

NOTE_OFF = 0x80
# 1000cccc 0nnnnnnn 0vvvvvvv (channel, note, velocity)

NOTE_ON = 0x90
# 1001cccc 0nnnnnnn 0vvvvvvv (channel, note, velocity)

AFTERTOUCH = 0xA0
# 1010cccc 0nnnnnnn 0vvvvvvv (channel, note, velocity)

CONTINUOUS_CONTROLLER = 0xB0  # see Channel Mode Messages!!!
# 1011cccc 0ccccccc 0vvvvvvv (channel, controller, value)

PATCH_CHANGE = 0xC0
# 1100cccc 0ppppppp (channel, program)

CHANNEL_PRESSURE = 0xD0
# 1101cccc 0ppppppp (channel, pressure)

PITCH_BEND = 0xE0
# 1110cccc 0vvvvvvv 0wwwwwww (channel, value-lo, value-hi)


###################################################
# Channel Mode Messages (Continuous Controller)
# They share a status byte.
# The controller makes the difference here

# High resolution continuous controllers (MSB)

BANK_SELECT = 0x00
MODULATION_WHEEL = 0x01
BREATH_CONTROLLER = 0x02
FOOT_CONTROLLER = 0x04
PORTAMENTO_TIME = 0x05
DATA_ENTRY = 0x06
CHANNEL_VOLUME = 0x07
BALANCE = 0x08
PAN = 0x0A
EXPRESSION_CONTROLLER = 0x0B
EFFECT_CONTROL_1 = 0x0C
EFFECT_CONTROL_2 = 0x0D
GEN_PURPOSE_CONTROLLER_1 = 0x10
GEN_PURPOSE_CONTROLLER_2 = 0x11
GEN_PURPOSE_CONTROLLER_3 = 0x12
GEN_PURPOSE_CONTROLLER_4 = 0x13

# High resolution continuous controllers (LSB)

BANK_SELECT = 0x20
MODULATION_WHEEL = 0x21
BREATH_CONTROLLER = 0x22
FOOT_CONTROLLER = 0x24
PORTAMENTO_TIME = 0x25
DATA_ENTRY = 0x26
CHANNEL_VOLUME = 0x27
BALANCE = 0x28
PAN = 0x2A
EXPRESSION_CONTROLLER = 0x2B
EFFECT_CONTROL_1 = 0x2C
EFFECT_CONTROL_2 = 0x2D
GENERAL_PURPOSE_CONTROLLER_1 = 0x30
GENERAL_PURPOSE_CONTROLLER_2 = 0x31
GENERAL_PURPOSE_CONTROLLER_3 = 0x32
GENERAL_PURPOSE_CONTROLLER_4 = 0x33

# Switches

SUSTAIN_ONOFF = 0x40
PORTAMENTO_ONOFF = 0x41
SOSTENUTO_ONOFF = 0x42
SOFT_PEDAL_ONOFF = 0x43
LEGATO_ONOFF = 0x44
HOLD_2_ONOFF = 0x45

# Low resolution continuous controllers

# (TG: Sound Variation;   FX: Exciter On/Off)
SOUND_CONTROLLER_1 = 0x46
# (TG: Harmonic Content;   FX: Compressor On/Off)
SOUND_CONTROLLER_2 = 0x47
# (TG: Release Time;   FX: Distortion On/Off)
SOUND_CONTROLLER_3 = 0x48
SOUND_CONTROLLER_4 = 0x49                  # (TG: Attack Time;   FX: EQ On/Off)
# (TG: Brightness;   FX: Expander On/Off)75	SOUND_CONTROLLER_6   (TG: Undefined;   FX: Reverb OnOff)
SOUND_CONTROLLER_5 = 0x4A
SOUND_CONTROLLER_7 = 0x4C                  # (TG: Undefined;   FX: Delay OnOff)
# (TG: Undefined;   FX: Pitch Transpose OnOff)
SOUND_CONTROLLER_8 = 0x4D
# (TG: Undefined;   FX: Flange/Chorus OnOff)
SOUND_CONTROLLER_9 = 0x4E
# (TG: Undefined;   FX: Special Effects OnOff)
SOUND_CONTROLLER_10 = 0x4F
GENERAL_PURPOSE_CONTROLLER_5 = 0x50
GENERAL_PURPOSE_CONTROLLER_6 = 0x51
GENERAL_PURPOSE_CONTROLLER_7 = 0x52
GENERAL_PURPOSE_CONTROLLER_8 = 0x53
# (PTC)   (0vvvvvvv is the source Note number)   (Detail)
PORTAMENTO_CONTROL = 0x54
EFFECTS_1 = 0x5B                           # (Ext. Effects Depth)
EFFECTS_2 = 0x5C                           # (Tremelo Depth)
EFFECTS_3 = 0x5D                           # (Chorus Depth)
EFFECTS_4 = 0x5E                           # (Celeste Depth)
EFFECTS_5 = 0x5F                           # (Phaser Depth)
DATA_INCREMENT = 0x60                      # (0vvvvvvv is n/a; use 0)
DATA_DECREMENT = 0x61                      # (0vvvvvvv is n/a; use 0)
NON_REGISTERED_PARAMETER_NUMBER = 0x62     # (LSB)
NON_REGISTERED_PARAMETER_NUMBER = 0x63     # (MSB)
REGISTERED_PARAMETER_NUMBER = 0x64         # (LSB)
REGISTERED_PARAMETER_NUMBER = 0x65         # (MSB)

# Channel Mode messages - (Detail)

ALL_SOUND_OFF = 0x78
RESET_ALL_CONTROLLERS = 0x79
LOCAL_CONTROL_ONOFF = 0x7A
ALL_NOTES_OFF = 0x7B
OMNI_MODE_OFF = 0x7C          # (also causes ANO)
OMNI_MODE_ON = 0x7D           # (also causes ANO)
MONO_MODE_ON = 0x7E           # (Poly Off; also causes ANO)
POLY_MODE_ON = 0x7F  # (Mono Off; also causes ANO)


###################################################
# System Common Messages, for all channels

SYSTEM_EXCLUSIVE = 0xF0
# 11110000 0iiiiiii 0ddddddd ... 11110111

MTC = 0xF1  # MIDI Time Code Quarter Frame
# 11110001

SONG_POSITION_POINTER = 0xF2
# 11110010 0vvvvvvv 0wwwwwww (lo-position, hi-position)

SONG_SELECT = 0xF3
# 11110011 0sssssss (songnumber)

#UNDEFINED = 0xF4
# 11110100

#UNDEFINED = 0xF5
# 11110101

TUNING_REQUEST = 0xF6
# 11110110

END_OFF_EXCLUSIVE = 0xF7  # terminator
# 11110111 # End of system exclusive


###################################################
# Midifile meta-events

SEQUENCE_NUMBER = 0x00      # 00 02 ss ss (seq-number)
TEXT = 0x01      # 01 len text...
COPYRIGHT = 0x02      # 02 len text...
SEQUENCE_NAME = 0x03      # 03 len text...
INSTRUMENT_NAME = 0x04      # 04 len text...
LYRIC = 0x05      # 05 len text...
MARKER = 0x06      # 06 len text...
CUEPOINT = 0x07      # 07 len text...
PROGRAM_NAME = 0x08      # 08 len text...
DEVICE_NAME = 0x09      # 09 len text...

MIDI_CH_PREFIX = 0x20      # MIDI channel prefix assignment (unofficial)

MIDI_PORT = 0x21      # 21 01 port, legacy stuff but still used
END_OF_TRACK = 0x2F      # 2f 00
TEMPO = 0x51      # 51 03 tt tt tt (tempo in us/quarternote)
SMTP_OFFSET = 0x54      # 54 05 hh mm ss ff xx
TIME_SIGNATURE = 0x58      # 58 04 nn dd cc bb
KEY_SIGNATURE = 0x59      # ??? len text...
SPECIFIC = 0x7F      # Sequencer specific event

FILE_HEADER = 'MThd'
TRACK_HEADER = 'MTrk'

###################################################
# System Realtime messages
# I don't supose these are to be found in midi files?!

TIMING_CLOCK = 0xF8
# undefined    = 0xF9
SONG_START = 0xFA
SONG_CONTINUE = 0xFB
SONG_STOP = 0xFC
# undefined    = 0xFD
ACTIVE_SENSING = 0xFE
SYSTEM_RESET = 0xFF


###################################################
# META EVENT, it is used only in midi files.
# In transmitted data it means system reset!!!

META_EVENT = 0xFF
# 11111111


###################################################
# Helper functions

def is_status(byte):
    return (byte & 0x80) == 0x80  # 1000 0000


#===================== DataTypeConverters.py ========================#

"""
This module contains functions for reading and writing the special data types
that a midi file contains.
"""

"""
nibbles are four bits. A byte consists of two nibles.
hiBits==0xF0, loBits==0x0F Especially used for setting
channel and event in 1. byte of musical midi events
"""


def getNibbles(byte):
    """
    Returns hi and lo bits in a byte as a tuple
    Asserts byte <= 255
    """
    return (byte >> 4 & 0xF, byte & 0xF)


def setNibbles(hiNibble, loNibble):
    """
    returns byte with value set according to hi and lo bits
    Asserts hiNibble <= 15 and loNibble <= 15
    """
    return (hiNibble << 4) + loNibble


def readBew(value):
    "Reads string as big endian word, (asserts len(value) in [1,2,4])"
    return unpack('>%s' % {1: 'B', 2: 'H', 4: 'L'}[len(value)], value)[0]


def writeBew(value, length):
    "Write int as big endian formatted string, (asserts length in [1,2,4])"
    return pack('>%s' % {1: 'B', 2: 'H', 4: 'L'}[length], value)


"""
Variable Length Data (varlen) is a data format sprayed liberally throughout
a midi file. It can be anywhere from 1 to 4 bytes long.
If the 8'th bit is set in a byte another byte follows. The value is stored
in the lowest 7 bits of each byte. So max value is 4x7 bits = 28 bits.
"""


def readVar(value):
    """
    Converts varlength format to integer. Just pass it 0 or more chars that
    might be a varlen and it will only use the relevant chars.
    use varLen(readVar(value)) to see how many bytes the integer value takes.
    asserts len(value) >= 0
    """
    sum = 0
    for byte in unpack('%sB' % len(value), value):
        sum = (sum << 7) + (byte & 0x7F)
        if not 0x80 & byte:
            break  # stop after last byte
    return sum


def varLen(value):
    """
    Returns the the number of bytes an integer will be when
    converted to varlength
    """
    if value <= 127:
        return 1
    elif value <= 16383:
        return 2
    elif value <= 2097151:
        return 3
    else:
        return 4


def writeVar(value):
    "Converts an integer to varlength format"
    sevens = to_n_bits(value, varLen(value))
    for i in range(len(sevens) - 1):
        sevens[i] = sevens[i] | 0x80
    return fromBytes(sevens)


def to_n_bits(value, length=1, nbits=7):
    "returns the integer value as a sequence of nbits bytes"
    bytes = [(value >> (i * nbits)) & 0x7F for i in range(length)]
    bytes.reverse()
    return bytes


def toBytes(value):
    "Turns a string into a list of byte values"
    return unpack('%sB' % len(value), value)


def fromBytes(value):
    "Turns a list of bytes into a string"
    if not value:
        return ''
    return pack('%sB' % len(value), *value)


#=================== RawOutstreamFile.py ============================#

class RawOutstreamFile:

    """

    Writes a midi file to disk.

    """

    def __init__(self, outfile=''):
        self.buffer = StringIO()
        self.outfile = outfile

    # native data reading functions

    def writeSlice(self, str_slice):
        "Reads the next text slice from the raw data, with length"
        self.buffer.write(str_slice)

    def writeBew(self, value, length=1):
        "Writes a value to the file as big endian word"
        self.writeSlice(writeBew(value, length))

    def writeVarLen(self, value):
        "Writes a variable length word to the file"
        var = self.writeSlice(writeVar(value))

    def write(self):
        "Writes to disc"
        if self.outfile:
            if isinstance(self.outfile, StringType):
                outfile = open(self.outfile, 'wb')
                outfile.write(self.getvalue())
                outfile.close()
            else:
                self.outfile.write(self.getvalue())

    def getvalue(self):
        return self.buffer.getvalue()


#=================== MidiOutStream.py ===============================#

class MidiOutStream:

    """

    MidiOutstream is Basically an eventhandler. It is the most central
    class in the Midi library. You use it both for writing events to
    an output stream, and as an event handler for an input stream.

    This makes it extremely easy to take input from one stream and
    send it to another. Ie. if you want to read a Midi file, do some
    processing, and send it to a midiport.

    All time values are in absolute values from the opening of a
    stream. To calculate time values, please use the MidiTime and
    MidiDeltaTime classes.

    """

    def __init__(self):

        # the time is rather global, so it needs to be stored
        # here. Otherwise there would be no really simple way to
        # calculate it. The alternative would be to have each event
        # handler do it. That sucks even worse!
        self._absolute_time = 0
        self._relative_time = 0
        self._current_track = 0
        self._running_status = None

    # time handling event handlers. They should overwritten with care

    def update_time(self, new_time=0, relative=1):
        """
        Updates the time, if relative is true, new_time is relative,
        else it's absolute.
        """
        if relative:
            self._relative_time = new_time
            self._absolute_time += new_time
        else:
            self._relative_time = new_time - self._absolute_time
            self._absolute_time = new_time

    def reset_time(self):
        """
        reset time to 0
        """
        self._relative_time = 0
        self._absolute_time = 0

    def rel_time(self):
        "Returns the relative time"
        return self._relative_time

    def abs_time(self):
        "Returns the absolute time"
        return self._absolute_time

    # running status methods

    def reset_run_stat(self):
        "Invalidates the running status"
        self._running_status = None

    def set_run_stat(self, new_status):
        "Set the new running status"
        self._running_status = new_status

    def get_run_stat(self):
        "Set the new running status"
        return self._running_status

    # track handling event handlers

    def set_current_track(self, new_track):
        "Sets the current track number"
        self._current_track = new_track

    def get_current_track(self):
        "Returns the current track number"
        return self._current_track

    #####################
    # Midi events

    def channel_message(self, message_type, channel, data):
        """The default event handler for channel messages"""
        pass

    def note_on(self, channel=0, note=0x40, velocity=0x40):
        """
        channel: 0-15
        note, velocity: 0-127
        """
        pass

    def note_off(self, channel=0, note=0x40, velocity=0x40):
        """
        channel: 0-15
        note, velocity: 0-127
        """
        pass

    def aftertouch(self, channel=0, note=0x40, velocity=0x40):
        """
        channel: 0-15
        note, velocity: 0-127
        """
        pass

    def continuous_controller(self, channel, controller, value):
        """
        channel: 0-15
        controller, value: 0-127
        """
        pass

    def patch_change(self, channel, patch):
        """
        channel: 0-15
        patch: 0-127
        """
        pass

    def channel_pressure(self, channel, pressure):
        """
        channel: 0-15
        pressure: 0-127
        """
        pass

    def pitch_bend(self, channel, value):
        """
        channel: 0-15
        value: 0-16383

        """
        pass

    #####################
    # System Exclusive

    def system_exclusive(self, data):
        """
        data: list of values in range(128)
        """
        pass

    #####################
    # Common events

    def song_position_pointer(self, value):
        """
        value: 0-16383
        """
        pass

    def song_select(self, songNumber):
        """
        songNumber: 0-127
        """
        pass

    def tuning_request(self):
        """
        No values passed
        """
        pass

    def midi_time_code(self, msg_type, values):
        """
        msg_type: 0-7
        values: 0-15
        """
        pass

    #########################
    # header does not really belong here. But anyhoo!!!

    def header(self, format=0, nTracks=1, division=96):
        """
        format: type of midi file in [1,2]
        nTracks: number of tracks
        division: timing division
        """
        pass

    def eof(self):
        """
        End of file. No more events to be processed.
        """
        pass

    #####################
    # meta events

    def meta_event(self, meta_type, data):
        """
        Handles any undefined meta events
        """
        pass

    def start_of_track(self, n_track=0):
        """
        n_track: number of track
        """
        pass

    def end_of_track(self):
        """
        n_track: number of track
        """
        pass

    def sequence_number(self, value):
        """
        value: 0-16383
        """
        pass

    def text(self, text):
        """
        Text event
        text: string
        """
        pass

    def copyright(self, text):
        """
        Copyright notice
        text: string
        """
        pass

    def sequence_name(self, text):
        """
        Sequence/track name
        text: string
        """
        pass

    def instrument_name(self, text):
        """
        text: string
        """
        pass

    def lyric(self, text):
        """
        text: string
        """
        pass

    def marker(self, text):
        """
        text: string
        """
        pass

    def cuepoint(self, text):
        """
        text: string
        """
        pass

    def midi_ch_prefix(self, channel):
        """
        channel: midi channel for subsequent data (deprecated in the spec)
        """
        pass

    def midi_port(self, value):
        """
        value: Midi port (deprecated in the spec)
        """
        pass

    def tempo(self, value):
        """
        value: 0-2097151
        tempo in us/quarternote
        (to calculate value from bpm: int(60,000,000.00 / BPM))
        """
        pass

    def smtp_offset(self, hour, minute, second, frame, framePart):
        """
        hour,
        minute,
        second: 3 bytes specifying the hour (0-23), minutes (0-59) and
                seconds (0-59), respectively. The hour should be
                encoded with the SMPTE format, just as it is in MIDI
                Time Code.
        frame: A byte specifying the number of frames per second (one
               of : 24, 25, 29, 30).
        framePart: A byte specifying the number of fractional frames,
                   in 100ths of a frame (even in SMPTE-based tracks
                   using a different frame subdivision, defined in the
                   MThd chunk).
        """
        pass

    def time_signature(self, nn, dd, cc, bb):
        """
        nn: Numerator of the signature as notated on sheet music
        dd: Denominator of the signature as notated on sheet music
            The denominator is a negative power of 2: 2 = quarter
            note, 3 = eighth, etc.
        cc: The number of MIDI clocks in a metronome click
        bb: The number of notated 32nd notes in a MIDI quarter note
            (24 MIDI clocks)
        """
        pass

    def key_signature(self, sf, mi):
        """
        sf: is a byte specifying the number of flats (-ve) or sharps
            (+ve) that identifies the key signature (-7 = 7 flats, -1
            = 1 flat, 0 = key of C, 1 = 1 sharp, etc).
        mi: is a byte specifying a major (0) or minor (1) key.
        """
        pass

    def sequencer_specific(self, data):
        """
        data: The data as byte values
        """
        pass

    #####################
    # realtime events

    def timing_clock(self):
        """
        No values passed
        """
        pass

    def song_start(self):
        """
        No values passed
        """
        pass

    def song_stop(self):
        """
        No values passed
        """
        pass

    def song_continue(self):
        """
        No values passed
        """
        pass

    def active_sensing(self):
        """
        No values passed
        """
        pass

    def system_reset(self):
        """
        No values passed
        """
        pass


#============================ MidiOutFile.py ========================#

class MidiOutFile(MidiOutStream):

    """
    MidiOutFile is an eventhandler that subclasses MidiOutStream.
    """

    def __init__(self, raw_out=''):

        self.raw_out = RawOutstreamFile(raw_out)
        MidiOutStream.__init__(self)

    def write(self):
        self.raw_out.write()

    def event_slice(self, slc):
        """
        Writes the slice of an event to the current track. Correctly
        inserting a varlen timestamp too.
        """
        trk = self._current_track_buffer
        trk.writeVarLen(self.rel_time())
        trk.writeSlice(slc)

    #####################
    # Midi events

    def note_on(self, channel=0, note=0x40, velocity=0x40):
        """
        channel: 0-15
        note, velocity: 0-127
        """
        slc = fromBytes([NOTE_ON + channel, note, velocity])
        self.event_slice(slc)

    def note_off(self, channel=0, note=0x40, velocity=0x40):
        """
        channel: 0-15
        note, velocity: 0-127
        """
        slc = fromBytes([NOTE_OFF + channel, note, velocity])
        self.event_slice(slc)

    def aftertouch(self, channel=0, note=0x40, velocity=0x40):
        """
        channel: 0-15
        note, velocity: 0-127
        """
        slc = fromBytes([AFTERTOUCH + channel, note, velocity])
        self.event_slice(slc)

    def continuous_controller(self, channel, controller, value):
        """
        channel: 0-15
        controller, value: 0-127
        """
        slc = fromBytes([CONTINUOUS_CONTROLLER + channel, controller, value])
        self.event_slice(slc)
        # These should probably be implemented
        # http://users.argonet.co.uk/users/lenny/midi/tech/spec.html#ctrlnums

    def patch_change(self, channel, patch):
        """
        channel: 0-15
        patch: 0-127
        """
        slc = fromBytes([PATCH_CHANGE + channel, patch])
        self.event_slice(slc)

    def channel_pressure(self, channel, pressure):
        """
        channel: 0-15
        pressure: 0-127
        """
        slc = fromBytes([CHANNEL_PRESSURE + channel, pressure])
        self.event_slice(slc)

    def pitch_bend(self, channel, value):
        """
        channel: 0-15
        value: 0-16383
        """
        msb = (value >> 7) & 0xFF
        lsb = value & 0xFF
        slc = fromBytes([PITCH_BEND + channel, msb, lsb])
        self.event_slice(slc)

    #####################
    # System Exclusive

#    def sysex_slice(sysex_type, data):
#        ""
#        sysex_len = writeVar(len(data)+1)
#        self.event_slice(SYSTEM_EXCLUSIVE + sysex_len + data + END_OFF_EXCLUSIVE)
#
    def system_exclusive(self, data):
        """
        data: list of values in range(128)
        """
        sysex_len = writeVar(len(data) + 1)
        self.event_slice(
            chr(SYSTEM_EXCLUSIVE) +
            sysex_len +
            data +
            chr(END_OFF_EXCLUSIVE))

    #####################
    # Common events

    def midi_time_code(self, msg_type, values):
        """
        msg_type: 0-7
        values: 0-15
        """
        value = (msg_type << 4) + values
        self.event_slice(fromBytes([MIDI_TIME_CODE, value]))

    def song_position_pointer(self, value):
        """
        value: 0-16383
        """
        lsb = (value & 0x7F)
        msb = (value >> 7) & 0x7F
        self.event_slice(fromBytes([SONG_POSITION_POINTER, lsb, msb]))

    def song_select(self, songNumber):
        """
        songNumber: 0-127
        """
        self.event_slice(fromBytes([SONG_SELECT, songNumber]))

    def tuning_request(self):
        """
        No values passed
        """
        self.event_slice(chr(TUNING_REQUEST))

    #########################
    # header does not really belong here. But anyhoo!!!

    def header(self, format=0, nTracks=1, division=96):
        """
        format: type of midi file in [0,1,2]
        nTracks: number of tracks. 1 track for type 0 file
        division: timing division ie. 96 ppq.

        """
        raw = self.raw_out
        raw.writeSlice('MThd')
        bew = raw.writeBew
        bew(6, 4)  # header size
        bew(format, 2)
        bew(nTracks, 2)
        bew(division, 2)

    def eof(self):
        """
        End of file. No more events to be processed.
        """
        # just write the file then.
        self.write()

    #####################
    # meta events

    def meta_slice(self, meta_type, data_slice):
        "Writes a meta event"
        slc = fromBytes([META_EVENT, meta_type]) + \
            writeVar(len(data_slice)) + data_slice
        self.event_slice(slc)

    def meta_event(self, meta_type, data):
        """
        Handles any undefined meta events
        """
        self.meta_slice(meta_type, fromBytes(data))

    def start_of_track(self, n_track=0):
        """
        n_track: number of track
        """
        self._current_track_buffer = RawOutstreamFile()
        self.reset_time()
        self._current_track += 1

    def end_of_track(self):
        """
        Writes the track to the buffer.
        """
        raw = self.raw_out
        raw.writeSlice(TRACK_HEADER)
        track_data = self._current_track_buffer.getvalue()
        # wee need to know size of track data.
        eot_slice = writeVar(self.rel_time()) + \
            fromBytes([META_EVENT, END_OF_TRACK, 0])
        raw.writeBew(len(track_data) + len(eot_slice), 4)
        # then write
        raw.writeSlice(track_data)
        raw.writeSlice(eot_slice)

    def sequence_number(self, value):
        """
        value: 0-65535
        """
        self.meta_slice(meta_type, writeBew(value, 2))

    def text(self, text):
        """
        Text event
        text: string
        """
        self.meta_slice(TEXT, text)

    def copyright(self, text):
        """
        Copyright notice
        text: string
        """
        self.meta_slice(COPYRIGHT, text)

    def sequence_name(self, text):
        """
        Sequence/track name
        text: string
        """
        self.meta_slice(SEQUENCE_NAME, text)

    def instrument_name(self, text):
        """
        text: string
        """
        self.meta_slice(INSTRUMENT_NAME, text)

    def lyric(self, text):
        """
        text: string
        """
        self.meta_slice(LYRIC, text)

    def marker(self, text):
        """
        text: string
        """
        self.meta_slice(MARKER, text)

    def cuepoint(self, text):
        """
        text: string
        """
        self.meta_slice(CUEPOINT, text)

    def midi_ch_prefix(self, channel):
        """
        channel: midi channel for subsequent data
        (deprecated in the spec)
        """
        self.meta_slice(MIDI_CH_PREFIX, chr(channel))

    def midi_port(self, value):
        """
        value: Midi port (deprecated in the spec)
        """
        self.meta_slice(MIDI_CH_PREFIX, chr(value))

    def tempo(self, value):
        """
        value: 0-2097151
        tempo in us/quarternote
        (to calculate value from bpm: int(60,000,000.00 / BPM))
        """
        hb, mb, lb = (value >> 16 & 0xff), (value >> 8 & 0xff), (value & 0xff)
        self.meta_slice(TEMPO, fromBytes([hb, mb, lb]))

    def smtp_offset(self, hour, minute, second, frame, framePart):
        """
        hour,
        minute,
        second: 3 bytes specifying the hour (0-23), minutes (0-59) and
                seconds (0-59), respectively. The hour should be
                encoded with the SMPTE format, just as it is in MIDI
                Time Code.
        frame: A byte specifying the number of frames per second (one
               of : 24, 25, 29, 30).
        framePart: A byte specifying the number of fractional frames,
                   in 100ths of a frame (even in SMPTE-based tracks
                   using a different frame subdivision, defined in the
                   MThd chunk).
        """
        self.meta_slice(SMTP_OFFSET, fromBytes(
            [hour, minute, second, frame, framePart]))

    def time_signature(self, nn, dd, cc, bb):
        """
        nn: Numerator of the signature as notated on sheet music
        dd: Denominator of the signature as notated on sheet music
            The denominator is a negative power of 2: 2 = quarter
            note, 3 = eighth, etc.
        cc: The number of MIDI clocks in a metronome click
        bb: The number of notated 32nd notes in a MIDI quarter note
            (24 MIDI clocks)
        """
        self.meta_slice(TIME_SIGNATURE, fromBytes([nn, dd, cc, bb]))

    def key_signature(self, sf, mi):
        """
        sf: is a byte specifying the number of flats (-ve) or sharps
            (+ve) that identifies the key signature (-7 = 7 flats, -1
            = 1 flat, 0 = key of C, 1 = 1 sharp, etc).
        mi: is a byte specifying a major (0) or minor (1) key.
        """
        self.meta_slice(KEY_SIGNATURE, fromBytes([sf, mi]))

    def sequencer_specific(self, data):
        """
        data: The data as byte values
        """
        self.meta_slice(SEQUENCER_SPECIFIC, data)


#============================ convenient function ===================#
# play a simple track (no pause, no overlap) on pys60
# track is in the form  [(note1, dur1), (note2, dur2), ...]
def play(track):
    m = MidiOutFile('C:\\out.mid')
    m.header()
    m.start_of_track()
    for note, dur in track:
        m.update_time(0)
        m.note_on(note=note)
        m.update_time(dur)
        m.note_off(note=note)
    m.update_time(0)
    m.end_of_track()
    m.eof()
    # os.startfile('C:\\out.mid')    # for PC
    import audio
    import e32
    s = audio.Sound.open('C:\\out.mid')
    s.play()
    while s.state() == 2:  # playing
        e32.ao_sleep(0.1)
    s.close()
