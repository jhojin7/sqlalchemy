- 실행  
`python3 automapping.py`

- 출력
```
user
[Column('id', INTEGER(), table=<user>, primary_key=True, nullable=False), Column('name', TEXT(), table=<user>, nullable=False), Column('password', TEXT(), table=<user>, nullable=False), Column('email', TEXT(), table=<user>, nullable=False), Column('isAdmin', INTEGER(), table=<user>)]
(0, 'user1', 'user1!', 'user1@sejong.ac.kr', 0)
(1, 'user2', 'user2@', 'user2@sju.ac.kr', 0)
(2, 'user3', 'user3#', 'user3@sejong.ac.kr', 1)
room
[Column('id', INTEGER(), table=<room>, primary_key=True, nullable=False), Column('name', TEXT(), table=<room>, nullable=False), Column('address', TEXT(), table=<room>, nullable=False)]
(0, '센835', '대양ai센터')
(1, '센836', '대양ai센터8층')
```
