# Documentation

# Table of Contents
1. [Gloves](#Gloves)
    1. [Data Collection](#Data-Collection)
    2. [Data Transmission](#Data-Transmission)
    3. [Power Supply](#Power-Supply)
    4. [Gloves](#Gloves)
2. [User App](#User-App)
    1. [Receiving](#Receiving)
    2. [Sending](#Sending)
    3. [Security](#Security)
    4. [GUI](#GUI)
3. [Server](#Server)
    1. [Why not Hosting Our Own Server?](#Why-not-Hosting-Our-Own-Server?)
    2. [Web Service Provider](#Web-Service-Provider)
    3. [Choose a Language](#Choose-a-Language)
    4. [Server Software](#Server-Software)
    5. [Database Software](#Database-Software)

# Gloves <a name="Data-Collection"></a>

## Data Collection

One idea is to use cameras to track the colored dots on gloves and interpret by image processing while it is severely affected by poor lighting conditions. It also involves too much about image processing which is far beyond our scope hence it is abandoned.

  The next idea is to use accelerometers. Accelerometers can do 3-axis acceleration measurements. Whenever the user does a gesture, there would be a force which distinctly depicts the movement by its magnitude and direction. The force is proportional to acceleration. The captured acceleration would then be converted to electronic signals by sensors.

  There are two kinds of accelerometer available on the market: analogue ones and digital ones. For analogue accelerometers, ADXL335 and ADXL377 would be investigated below. The output signals would be 3 pins for x-axis acceleration, y -axis acceleration and z-axis acceleration. In total, 30 analogue input pins would be needed on the microcontroller. However, on the market, the number of analogue pins would be harder to meet requirements than that of digital pins. For example, ATmega2560\cite{arduino_mega} has 16 analogue pins and 54 digital pins and ATSAMD21G18\cite{arduino_genuino} has 6 analogue pins and 20 digital pins. Moreover, analogue signals would eventually be converted to digital signals for the ease of processing data by a ADC module inside the microprocessor. Features of ADXL377 are much better than those of ADXL335. ADXL377 has a much higher sensitivity of 6.5mV/g, which is better than ADXL335’s, 300mV/g. All other features are almost the same. However, ADXL377 bears a much higher price, £21, than £2.2, the price of ADXL335. If all ten sensors implement ADXL377, the cost would be extremely high. So ADXL335 would be implemented if sensors are all analogue ones.

  If sensors are digital ones, ADXL362(£2.99) would be considered. The acceleration would be represented by either 12-bit or 8-bit. ADC modules inside microcontrollers can be omitted for the implementation of digital accelerometers. Digital accelerators can have multiple modes to fit a range of work: mode for continuous, wide bandwidth sensing; and wake-up mode for limited bandwidth activity detection. In wake-up mode, the power consumption is extremely low because it allows the rest of the system powered down until an activity is detected. In the case of ADXL362, the supply voltage is 2V. Power consumption is quite low: working current is 270nA motion activated wake-up mode and 10nA standby current which is the current when the device is in sleep mode.

  As a result, power consumption is much lower than the analogue device. The wakeup mode is quite suitable for the sign language gloves: the user would not always have inputs to gloves. Sensitivity of ADXL362 is 1mg/LSB which can be derived to be 488mV/g if the power supply is 2V. This is slightly lower than ADXL335. The noise performance of ADXL362 in normal mode in X and Y output is 550µg/√Hz, in Z output 920µg/√Hz. The noise performance of the analogue ones is much better: 150µg/√Hz for X and Y output and 300µg/√Hz for Z output. However, the noise performance of ADXL362 can be improved by switching to low noise mode or ultralow noise mode, decreasing the noise level to 400µg/√Hz and 250µg/√Hz in X and Y output respectively. If the high noise makes extraordinary errors in the practical implementation, switching noise modes can improve the performance with an expense of higher power consumption. But ADXL362 has low complexity. The integrated digital chip would contain 5 more sections within the same chip area: axis demodulation, antialiasing filter, temperature sensors, ADC and SPI. More considerations about sampling frequency and designs about filters to keep from aliasing would be necessary in an analogue design. Moreover, decoupling capacitors and resisters would be included to ensure that there would not be much noise from the power supply.

  The analogue accelerometer of similar cost would have more accurate performance but much higher power consumption (~100 times) and design complexity. The trade-off between performance, complexity and power consumption would be considered more detailed in later practical experiments using different power supplies.

  The last idea is to use flex sensors. A flex sensor is a strip of material. The more it bends, the higher resistance it would possess. A linear relationship exists between them. As a result, it can form a potential divider by adding a resistor to reflect how it bends. Only those gestures without arm or elbow movements can be interpreted by flex sensors. For those sign languages involving hand movement. One extra accelerometer on each back of hand would detect the whole hand movement.

  No specific data about sensitivity about the flex sensor because its sensitivity is not determined by itself but how the overall circuit is designed. The circuit would bring errors. Output voltage would be an
  analogue signal as shown in Figure 1. The analogue signal would be fed into the analogue pin of a microcontroller and converted to digital signal inside the microcontroller.
  
## Data Transmission

The communication between the sensors and the microcontroller can be done using SPI or I2C interface. Both of them allow short-distance data transmission in serial form and are commonly used in commercial products. The main difference between SPI and I2C is the relationship between the master devices and the slave devices.

  For I2C devices, multiple slave devices can communicate with multiple master devices at the same time. While for SPI devices, multiple slave devices can only communicate with one master device at one time. For this project, only one master device, which is the microcontroller, is available. Hence it makes no difference using either SPI or I2C.

  The communication between the electronics on the gloves and the smart devices or PCs is either Bluetooth or WiFi. Using WiFi can transmit data at higher speed and over a longer distance. The drawback is high power consumption. Also the direct connection between devices using WiFi is more stable and supports encryption such as AES or WPA.

  Using Bluetooth is almost the opposite of using WiFi. Bluetooth supports shorter distance data transmission with lower power consumption and slower transmission speed. Bluetooth does support data encryption during transmission however the maximum length of key is 128 bits while WiFi supports up tp 256-bit encryption.

  Either Bluetooth or WiFi requires different hardware: we can use ESP8266 for WiFi and HC05 for Bluetooth. The specific power consumption rate is to be found in real tests. That is, we are going to test on using both Bluetooth and WiFi and choose the one with lower power consumption as well as satisfying the required data transmissions speed.

## Power Supply

A rechargeable Lithium ion 3.3V battery is preferred and available whose cost is £10. The cost is acceptable.

## Gloves

Gloves should always be normal gloves. The choice of colours would be decided by doing target customer surveys. There would be three sizes available small, 9 inches (22.86cm), medium, 10 inches(25.40cm) and large, 12 inches(30.48cm). Specific size of gloves can be produced if there would be special needs. Material used for the gloves could be cotton as cotton is comfortable and a good breathable  material, thus reduces hand perspiration when wearing the gloves.

  A PCB with a microcontroller is attached on the wrist connected with each sensor by wires. All of electronic components are fixed on a plastic layer which can be attached or detached from the pair of gloves by Velcro which is the material in Figure 2. Regular cleaning can be conducted by users without going to a professional.

# User App

The user app has four parts:receiving data from hardware, communicating processed data with the server, encryption/decryption when transmitting data over the Internet, GUI. In the early stage of development, a C++/Python will be used and will migrate to Android/iOS app in later stages.

## Receiving

The first part is to reveice real-time data from the hardware. Data will be sent from the Arduino in vector or matrix via Bluetooth or WiFi, depending on the hardware choice. Then, the user app will standardize the raw data received into different blocks, which depends on the gesture done by the user. This standardization is relevant since it simplifies the retrieving algorithm and speeds up the retrieving process.

## Sending

The second part handles the communication with the database. Blocks of data, previously divided, will be sent to the database so it can be processed by algorithms which will remove the unwanted noise and match with the corresponding word. Once data has been processed they will be sent back in the form of words.

## Security

The third part ensures secure transmission and prevents information being leaked by malicious attacks. Popular encryption algorithms can be grouped into being symmetric and asymmetric. Symmetric algorithms include DES, 3DES and AES. Asymmetric algorithms include DSA, RSA and X25519 key exchange.

## GUI

  The last part, will feed the word obtained from the server into a GUI. This interface will visualize and vocalize the received words. It can be implemented in three ways; in Python using the TkInter library under x86 platform, Android/iOS app under smart device environment. The smart device apps (i.e. Android and iOS app) are more socially appreciated since according to data, both operating systems account for a combined of 99.1% of the worldwide smartphone OS market.

# Server

## Why not Hosting Our Own Server?

A professional server needs reliable firewall, i.e. anti-DDoS

  A powerful server will consume lots of electricity and dissipate lots of heat. Additional facility, for instance, air conditioning, may be needed for reliable operation. Also, potential fire hazard exists since the machine is consuming lots of energy.

  Server hardware is expensive to obtain, i.e. DDR4 ECC Memory with the same clock frequency and the same size may be more expensive compared with regular DDR4 non-ECC memory. A brand new Xeon CPU is usually more expensive than a used core i7 CPU.

  Server hardware prioritizes reliability over performance. The hardware that we have, i.e. our desktops and laptops, prioritize performance over reliability. We can use our computers for testing and development, but not for real-world deployment.

  Cannot guarantee the connectivity and reliability of Internet if hosting the server and the database on our own.

  Microsoft, Amazon, Google and Aliyun operate dedicated/virtual server rental on a large-scale hence the cost is a lot lower.

## Web Service Provider

Select a web service provider, i.e. Microsoft Azure, Amazon Web Services, Google Cloud Platform, Aliyun, etc.

  In our early stage of development, different providers offer free-trials. For instance, using AWS, the first year is charge-free. However, certain limitations apply here. The RAM on rented server may not be enough and the disk storage is low. We may need to consider/compare different offers.

  There are a number of factors to be considered when choosing a web service provider: cost per hour, CPU types/generation, CPU clock frequency, CPU L3 cache, size of the RAM, size of the hard disk, location of the server, dedicated server or virtual server.

  Also, different providers’ offers vary in terms of available services, i.e. availability of certain kinds of dynamic web application deployment, which enables us to minimize the cost.

## Choose a Language

  Choose a language and write the server-side program which will control the data flow and communicate with the database

## Server Software

The server software can communicate with the device that is sending the parsed/partially processed information via Internet. The server can receiving income information and sending the fully processed information back to the device.

  The software should support encrypted data transmission. The data sent between the device and the server software are encrypted for security. For instance, using asymmetric algorithm like RSA for encryption and decryption. To enhance security, the server software also supports administrative features: remote administrator login, backup, status check, logging, log check, user information and activities recording, etc.

  The server software can parse and process the incoming information from the user-end into SQL instructions so that the database can understand and retrieve the translated information. The server can handle large amount inbound requests and outbound data, when processing requests from multiple devices at the same time instead of just one device at a time. To further increase the speed of processing requests, non-blocking features will be adopted. The execution in the server software is multi-threaded.

  The server should be simple to deploy. The final server software is in an executable package. Hence there is no need for excessively configuring the running environment.

  The data delivered to the user app are in a parsed form, i.e. HTML file or other forms if applicable.

  OOP features are used. Just to make the code easy to analyse and upgrade.

## Database Software <a name="Database-Software"></a>

Note here that we want to run the server-side program and the database on the same rented server, just for decreasing the delay caused by the communication with the server and the database.

  In the case that the database is expanding, and a more powerful/reliable server is needed, we may want to consider separating the database from the dedicated server and add some redundancy to both the server and the database, for reliability issues. In case of a failure, other servers will quickly replace the failed server.

  We need to choose a database software or a database package that comes with the language that we used to program the server software, i.e. Microsoft SQL Server, MySQL, or MongoDB package for Node.js, with the following considerations.
  
  The operating system that the database is running on, i.e. Windows, Mac, Unix, if Linux, which distribution, i.e. Fedora, Linux Mint, Ubuntu, CentOS, etc
  Is a GUI needed for database?
  
  Compatibility with the hardware, i.e. are there any restrictions on the minimum RAM/CPU clock frequency requirements?
  
  Licence issues. For instance, Microsoft SQL Server may require a licence for large-scale application and if used for profit
  
  Reliability, i.e. are there lots of people who are currently using the software? Is there a huge community that maintains and provides help for the database software.
  
  Ease to use, i.e. is it hard to write program that will operate on the database? When writing the server software, are there any drivers needed for communicating, i.e. if we are using Java for the server software and Microsoft SQL Server on the server, additional driver is needed, either provided by third party communities/personnel, or officially by Oracle or Microsoft. Using such kind of additional software may/may not add the level difficulty to the development/implementation.
