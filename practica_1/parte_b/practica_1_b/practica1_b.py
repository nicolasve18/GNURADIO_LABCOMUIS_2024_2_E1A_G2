#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: configuracionUSAP
# GNU Radio version: 3.10.10.0

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time



class practica1_b(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "configuracionUSAP", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("configuracionUSAP")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "practica1_b")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 200k
        self.fc = fc = 50M
        self.a = a = 500m
        self.GX = GX = 0

        ##################################################
        # Blocks
        ##################################################

        self.uhd_usrp_sink_0 = uhd.usrp_sink(
            ",".join(("", '')),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
            "",
        )
        self.uhd_usrp_sink_0.set_samp_rate(200k)
        self.uhd_usrp_sink_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)

        self.uhd_usrp_sink_0.set_center_freq(0, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_sink_0.set_gain(0, 0)
        self._fc_range = qtgui.Range(50M, 2.2G, 1M, 50M, 200)
        self._fc_win = qtgui.RangeWidget(self._fc_range, self.set_fc, "frecuencia portadora", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fc_win)
        self.analog_const_source_x_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 500m)
        self._a_range = qtgui.Range(0, 1, 100u, 500m, 200)
        self._a_win = qtgui.RangeWidget(self._a_range, self.set_a, "amplitud señal TX", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._a_win)
        self._GX_range = qtgui.Range(0, 30, 1, 0, 200)
        self._GX_win = qtgui.RangeWidget(self._GX_range, self.set_GX, "ganacia del TX", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._GX_win)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.uhd_usrp_sink_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "practica1_b")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc

    def get_a(self):
        return self.a

    def set_a(self, a):
        self.a = a

    def get_GX(self):
        return self.GX

    def set_GX(self, GX):
        self.GX = GX




def main(top_block_cls=practica1_b, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
