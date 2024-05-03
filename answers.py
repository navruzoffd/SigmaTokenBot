class Answers:

    @classmethod
    async def start(cls):
        message = f"""
<b>AIRDROP SIGMA COIN</b>
<b>100 $SIGMA</b> \U0001F4AA за каждого друга.
Скоро запуск на <b>TON</b> будь начеку..."""
        return message
    
    @classmethod
    async def invited_start(cls, name, referrer):
        message = f"""
Привет <b>{name}</b>! Вас пригласил <b>{referrer}</b>.
Начисляем вам <b>100 $SIGMA</b> \U0001F4AA"""
        return message
    
    @classmethod
    async def wrong_link(cls):
        message = """
\u2139 Некорректная ссылка."""
        return message
    
    @classmethod
    async def exist_user(cls):
        message = """
\u2139 Вы уже являетесь пользователем этого бота."""
        return message
    
    @classmethod
    async def wrong_user(cls):
        message = """
\u2139 Пригласившего вас пользователя не существует."""
        return message
    
    @classmethod
    async def balance_info(cls, balance):
        message = f"""
Ваш баланс <b>{balance} $SIGMA</b>
<i>1 друг = 100 $SIGMA</i>
Выполняй задания и приглашай друзей,
чтобы получить больше \U0001F4CB"""
        return message
    
    @classmethod
    async def invite_friends(cls, referrals, id_tg):
        message = f"""
Приглашено пользователей: <u>{referrals}</u>
Получай <b>100 $SIGMA</b> за каждого \U0001F4AA
<i>Ваша ссылка для приглашения</i>:

https://t.me/tokensigmatestbot?start={id_tg}"""
        return message
    
    @classmethod
    async def tasks(cls):
        message = """
Получите <b>200 $SIGMA</b> \U0001F4AA"""
        return message
    
    @classmethod
    async def msg_to_referrer(cls, referral):
        message = f"""
Пользователь <b>{referral}</b> перешёл по вашей ссылке!
Начисляем <b>100 $SIGMA</b> \U00002705"""
        return message
    
    @classmethod
    async def share_link(cls, id_tg):
        message = f"""
        
Запусти бота, и получи 100 $SIGMA токенов!
https://t.me/tokensigmatestbot?start={id_tg}"""
        return message
