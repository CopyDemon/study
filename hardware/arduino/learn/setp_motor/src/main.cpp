#include <Arduino.h>
#include <Stepper.h>


const int stepsPerRevolution = 2048;
const int buttonPin = 2; // 按钮连接到数字引脚2
bool isMotorRunning = false; // 电机是否正在运行的状态

Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);

void setup() {
  pinMode(buttonPin, INPUT_PULLUP); // 设置按钮引脚为输入并启用内部上拉电阻

  myStepper.setSpeed(5);  // 设置转速为 15 RPM
  Serial.begin(9600);
}

void loop() {
  // button logic
  // int buttonState = digitalRead(buttonPin);


  // // 马达代码
  // Serial.println("顺时针旋转一圈");
  // myStepper.step(stepsPerRevolution);
  // delay(1000);

  // Serial.println("逆时针旋转一圈");
  // myStepper.step(-stepsPerRevolution);
  // delay(1000);

  digitalWrite(2, HIGH); // 启动电机
  delay(1000);            // 延时1秒
  digitalWrite(2, LOW);  // 熄灭电机
  delay(1000);            // 延时1秒
}