# AHK
AHK helper

In AutoHotKey the % symbol is how they mark the start and end of a variable. In some recent use cases, I have wanted to set up an autohotkey to open up various internal websites. Those address strings would have % in them and cause issues with the AHK script. In order to make it work, one needs to escape them out witht he < ` > character. Not too big a deal if there is a one or two % characters in the address string. But if there is a lot and you don't want to miss any you can just paste the string into this python program and then paste the returned escaped string to your AHK script.

Won't work

send, http://www.some_Address.com/asp%strings%with%sIn%Them

return

Will work

send, http://www.some_Address.com/asp`%strings`%with`%sIn`%Them

return
