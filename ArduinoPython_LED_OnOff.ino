void setup() 
{
  pinMode(13, OUTPUT); // configura a porta 13 como output
  Serial.begin(9600);  // configura comunicaçao serial
}

void loop() 
{
  if(Serial.available()) // verifica se há conexão
  {
    char serialMsg = Serial.read(); // recebe a mensagem recebida pela comunicação serial
    if (serialMsg == 'H') // se receber H, liga o led. Caso receba L, desliga
    {
      digitalWrite(13, HIGH);
    }
    else if(serialMsg == 'L')
    {
      digitalWrite(13, LOW);
    }
  }
}
