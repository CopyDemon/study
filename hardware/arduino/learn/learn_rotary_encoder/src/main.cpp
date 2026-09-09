#include <Arduino.h>

// put function declarations here:
const int pinCLK = 2;
const int pinDT = 3;
const int pinSW = 4;
int volume = 0;

const int ledPin = 13; // Uno 板子上内置的LED灯

int lastCLK = HIGH;

void setup() {
  // put your setup code here, to run once:
  pinMode(pinCLK, INPUT_PULLUP); //clock pin 时钟
  pinMode(pinDT, INPUT_PULLUP); //data pin 数据
  pinMode(pinSW, INPUT_PULLUP); //switch pin 按钮

  pinMode(13, OUTPUT); // uno 板子上内置的led灯
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int currentCLK = digitalRead(pinCLK);

  // 简单检测旋钮旋转， 并模拟给出音量变化
  if(currentCLK != lastCLK && currentCLK == LOW){
    if(digitalRead(pinDT) == HIGH){
      // Serial.println("turning to right");
      volume++;
      if(volume < 100){
        Serial.println("Volume: " + String(volume));
      }else{
        Serial.println("Volume is at maximum (100). Cannot increase further.");
        volume = 100; // 限制最大音量为100
      }
      
      digitalWrite(ledPin, HIGH); // 右转旋钮点亮led
    }else{
      // Serial.println("turning to left");
      if(volume > 0){
        volume--;
        Serial.println("Volume: " + String(volume));
      }else{
        Serial.println("Volume is at minimum (0). Cannot decrease further.");
        volume = 0; // 限制最小音量为0
      }
      digitalWrite(ledPin, LOW); // 左转旋钮熄灭led
    }
  }

  lastCLK = currentCLK;

  // 简单模拟旋钮按下事件
  if (digitalRead(pinSW) == LOW) {
    Serial.println("Button Pressed");
    delay(200); // 简单防抖
  }
}