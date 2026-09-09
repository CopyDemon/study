#include <Arduino.h>

void setup() {
    pinMode(13, OUTPUT); // 设置数字13号引脚为输出模式
}

void loop() {
    digitalWrite(13, HIGH); // 点亮LED
    delay(1000);            // 延时1秒
    digitalWrite(13, LOW);  // 熄灭LED
    delay(1000);            // 延时1秒
}