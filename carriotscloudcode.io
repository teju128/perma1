#include “ESP8266WiFi.h”
 
const char* WiFiNetworkName = “teja”;
 
const char* NetworkPassword = “123456”;
 
const char* ServerName = “api.carriots.com”;
 
const String CARRIOTSAPI = “<API Key of Carriots>”;
 
const String DEVICE = “iotdevice@teja”;
 
WiFiClient client;
 
int readval = 0;
 
void setup() {
 
Serial.begin(9600);
 
delay(1000);
 
Serial.println();
 
Serial.print(“Connecting to Network”);
 
Serial.println(WiFiNetworkName);
 
WiFi.begin(WiFiNetworkName, NetworkPassword);
 
while (WiFi.status()!= WL_CONNECTED) {
 
delay(1000);
 
}
 
Serial.println(“Connected”);
 
}
 
void sendStream()
 
{
 
if (client.connect(ServerName, 80)) {
 
Serial.println(F(“connected”));
 
String json = “{\”protocol\”:\”v2\”,\”device\”:\”” + DEVICE + “\”,\”at\”:\”now\”,\”data\”:{\”RecordedData\”:\”” + val + “\”}}”;
 
client.println(“POST /streams HTTP/1.1”);
 
client.println(“Host: api.carriots.com”);
 
client.println(“Accept: application/json”);
 
client.println(“User-Agent: Arduino-Carriots”);
 
client.println(“Content-Type: application/json”);
 
client.print(“carriots.CarriotsAPI: “);
 
client.println(CARRIOTSAPI);
 
client.print(“Content-Length: “);
 
int thisLength = json.length();
 
client.println(thisLength);
 
client.println(“Connection: close”);
 
client.println();
 
client.println(json);
 
}
 
else { Serial.println(F(“Not Connected”)); }
 
}
 
void loop() {
 
readval = analogRead(A0);
 
Serial.println(val);
 
Serial.println(F(“Transmit Data”));
 
sendStream();
 
delay(1000);
 
}
