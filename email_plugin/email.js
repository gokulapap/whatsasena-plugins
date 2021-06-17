const Asena = require('../events');
const {MessageType} = require('@adiwajshing/baileys');
const got = require('got');
const Config = require('../config');

Asena.addCommand({pattern: 'readmail ?(.*)', fromMe: false, dontAddCommandList: true}, (async (message, match) => {

	var info = await message.reply('```Fetching all your recent mails...```');
	const url = `https://whatemail.herokuapp.com/readmail`;
	const response = await got(url);

	await message.client.sendMessage(message.jid, response.body, MessageType.text);

}));
