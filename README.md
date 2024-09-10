# diversity-slack-bot-sniffer

The Diversity bot (https://github.com/AugustoPinheiro/diversity-slack-bot) only analyzes messages in the public Slack channels it's a part of, but it doesn't join newly created channels. The sniffer has Event Subscriptions configured to receive alerts about created channels. Upon receiving a new channel, it analyzes, collects the name, joins, and notifies specific channels as defined in the configuration.

## Sniffer Configuration in Slack
Create bots in Slack with the following configurations:

### OAuth & Permissions
### Bot Token Scopes
* channels:read

### User Token Scopes
* channels:read

## Event Subscriptions
### Subscribe to bot events
* channel_created
-----
# diversity-slack-bot-farejador

O Diversity bot (https://github.com/AugustoPinheiro/diversity-slack-bot) apenas analisa as mensagens dos canais públicos de Slack que faz parte, mas não entra nos canais novos que forem criados. O farejador tem configurado o Event Subscrptions para receber alertas de canais criados. Ao receber um novo canal, ele analisa coleta o nome, entra e notifica em canais específicados na configuração.

## Configurações do Farejador no Slack
Crie os bots no Slack com as configuraçoes abaixo:

## OAuth & Permissions
### Bot Token Scopes
* channels:read

### User Token Scopes
* channels:read

## Event Subscriptions
### Subscribe to bot events
* channel_created

