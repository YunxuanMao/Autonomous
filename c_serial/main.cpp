#include <string>
#include <iostream>

#include <boost/asio.hpp>
#include <boost/bind.hpp>

using namespace std;
using namespace boost::asio;
unsigned char buf1[10];
io_service iosev;
serial_port sp(iosev, "/dev/ttyUSB0");

int main(int argc, char *argv[]) {
    sp.set_option(serial_port::baud_rate(115200));
    sp.set_option(serial_port::flow_control());
    sp.set_option(serial_port::parity());
    sp.set_option(serial_port::stop_bits());
    sp.set_option(serial_port::character_size(8));

    return 0;
}