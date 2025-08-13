# Common Telegram Bot API Endpoints

This document provides a reference list of commonly used endpoints (methods) in the [Telegram Bot API](https://core.telegram.org/bots/api). Each endpoint is accessed using the following pattern:

```
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/<METHOD_NAME>
```

Replace `<YOUR_BOT_TOKEN>` with your bot's token.

---

## Common Endpoints

| Method                   | Purpose                                                                |
|--------------------------|------------------------------------------------------------------------|
| `getMe`                  | Get information about your bot.                                        |
| `getUpdates`             | Receive incoming updates using long polling (messages, commands, etc). |
| `sendMessage`            | Send text messages.                                                    |
| `sendPhoto`              | Send photos.                                                           |
| `sendAudio`              | Send audio files.                                                      |
| `sendDocument`           | Send general files (PDF, ZIP, etc).                                    |
| `sendVideo`              | Send video files.                                                      |
| `sendAnimation`          | Send animation files (GIF, MPEG-4, etc.).                             |
| `sendVoice`              | Send voice messages.                                                   |
| `sendVideoNote`          | Send round video messages.                                             |
| `sendLocation`           | Send location information.                                             |
| `sendVenue`              | Send information about a venue.                                        |
| `sendContact`            | Send phone contacts.                                                   |
| `sendPoll`               | Send polls.                                                            |
| `sendDice`               | Send dice, dartboard, basketball, etc.                                 |
| `forwardMessage`         | Forward messages from one chat to another.                             |
| `copyMessage`            | Copy messages without a link to the original sender.                   |
| `editMessageText`        | Edit text messages.                                                    |
| `editMessageCaption`     | Edit message captions.                                                 |
| `deleteMessage`          | Delete messages.                                                       |
| `answerCallbackQuery`    | Respond to callback queries from inline keyboards.                     |
| `setWebhook`             | Set a webhook for receiving updates via HTTPS POST.                    |
| `deleteWebhook`          | Remove webhook integration.                                            |
| `getWebhookInfo`         | Get current webhook status.                                            |
| `getChat`                | Get information about a chat.                                          |
| `getChatAdministrators`  | Get a list of chat admins.                                             |
| `getChatMember`          | Get information about a member of a chat.                              |
| `getChatMembersCount`    | Get the number of members in a chat.                                   |
| `leaveChat`              | Leave a group, supergroup or channel.                                  |
| `sendSticker`            | Send stickers.                                                         |
| `sendGame`               | Send a game.                                                           |
| `setMyCommands`          | Set list of bot commands.                                              |
| `getMyCommands`          | Get list of bot commands.                                              |

---

## Usage Example

To send a message:
```
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/sendMessage
```

To get bot info:
```
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getMe
```

---

## References

- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
- [Available Telegram Bot API Methods](https://core.telegram.org/bots/api#available-methods)
