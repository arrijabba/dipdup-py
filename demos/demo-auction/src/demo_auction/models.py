from enum import IntEnum

from tortoise import fields
from tortoise.fields.relational import ForeignKeyFieldInstance

from dipdup.models import Model


class AuctionStatus(IntEnum):
    ACTIVE = 0
    FINISHED = 1


class User(Model):
    address = fields.CharField(36, pk=True)


class Token(Model):
    id = fields.BigIntField(pk=True)
    address = fields.CharField(36)
    amount = fields.BigIntField()
    level = fields.BigIntField()
    timestamp = fields.DatetimeField()
    holder: ForeignKeyFieldInstance[User] = fields.ForeignKeyField('models.User', 'tokens')

    token_id: int


class Auction(Model):
    id = fields.BigIntField(pk=True)
    token: ForeignKeyFieldInstance[Token] = fields.ForeignKeyField('models.Token', 'auctions')
    bid_amount = fields.BigIntField()
    bidder: ForeignKeyFieldInstance[User] = fields.ForeignKeyField('models.User', 'winning_auctions')
    seller: ForeignKeyFieldInstance[User] = fields.ForeignKeyField('models.User', 'created_auctions')
    end_timestamp = fields.DatetimeField()
    status = fields.IntEnumField(AuctionStatus)
    level = fields.BigIntField()
    timestamp = fields.DatetimeField()

    token_id: int


class Bid(Model):
    id = fields.BigIntField(pk=True)
    auction: ForeignKeyFieldInstance[Auction] = fields.ForeignKeyField('models.Auction', 'bids')
    bid_amount = fields.BigIntField()
    bidder: ForeignKeyFieldInstance[User] = fields.ForeignKeyField('models.User', 'bids')
    level = fields.BigIntField()
    timestamp = fields.DatetimeField()
