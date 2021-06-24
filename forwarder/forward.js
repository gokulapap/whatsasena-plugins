const Asena = require('../events');
const {MessageType, MessageOptions, Mimetype} = require('@adiwajshing/baileys');

Asena.addCommand({pattern: 'forward ?(.*)', fromMe: false, dontAddCommandList: true}, (async (message, match) => {
    if (match[1] === '') return await message.sendMessage('```Need message!```');

    var info = await message.reply('```sending message to all jids...```');

    message.client.sendMessage('{jid of the group/ user}', match[1], MessageType.text);
    
    //add as much as you want you can even add 100 jids and forward same message to 100 people at a time

    var info = await message.reply('```sent messages to everyone sucessfully !```');

}));
