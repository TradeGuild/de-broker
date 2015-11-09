import sqlalchemy as sa
import sqlalchemy.orm as orm
from flask.ext.login import UserMixin
from sqlalchemy_login_models.model import Base, UserKey, User as SLM_User


__all__ = ['Quote', 'Currency']


class QuoteRequest(Base):
    """A Request for a quote to convert one currency to another."""
    __tablename__ = "quote_request"
    __name__ = "quote_request"

    id = sa.Column(sa.Integer, primary_key=True, doc="primary key")
    asset_specified = sa.Column(sa.Enum("in", "out"))
    in_amount = sa.Column(sa.BigInteger, nullable=False)
    out_amount = sa.Column(sa.BigInteger, nullable=False)

    # foreign key reference to the input currency
    in_currency_code = sa.Column(
        sa.String,
        sa.ForeignKey('currency.code'),
        nullable=False)
    in_currency = orm.relationship("Currency", foreign_keys=[in_currency_code])

    # foreign key reference to the output currency
    out_currency_code = sa.Column(
        sa.String,
        sa.ForeignKey('currency.code'),
        nullable=False)
    out_currency = orm.relationship("Currency", foreign_keys=[out_currency_code])

    # foreign key reference to the owner of this coin's API key
    user_id = sa.Column(
        sa.Integer,
        sa.ForeignKey('user.id'),
        nullable=False)
    user = orm.relationship("User", foreign_keys=[user_id])

    def __init__(self, in_amount, in_currency_code, 
                 out_amount, out_currency_code, user_id):
        if in_amount > 0:
            self.in_amount = in_amount
            self.asset_specified = 'in'
            self.out_amount = 0
        elif out_amount > 0:
            self.out_amount = out_amount
            self.asset_specified = 'out'
            self.in_amount = 0
        self.in_currency_code = in_currency_code
        self.out_currency_code = out_currency_code
        self.user_id = user_id


class Quote(Base):
    """A Quote to convert one currency to another."""
    __tablename__ = "quote"
    __name__ = "quote"

    id = sa.Column(sa.Integer, primary_key=True, doc="primary key")
    in_amount = sa.Column(sa.BigInteger, nullable=False)
    out_amount = sa.Column(sa.BigInteger, nullable=False)

    # foreign key reference to the input currency
    in_currency_code = sa.Column(
        sa.String,
        sa.ForeignKey('currency.code'),
        nullable=False)
    in_currency = orm.relationship("Currency", foreign_keys=[in_currency_code])

    # foreign key reference to the output currency
    out_currency_code = sa.Column(
        sa.String,
        sa.ForeignKey('currency.code'),
        nullable=False)
    out_currency = orm.relationship("Currency", foreign_keys=[out_currency_code])

    # foreign key reference to the owner of this coin's API key
    user_id = sa.Column(
        sa.Integer,
        sa.ForeignKey('user.id'),
        nullable=False)
    user = orm.relationship("User", foreign_keys=[user_id])

    def __init__(self, in_amount, in_currency_code, 
                 out_amount, out_currency_code, user_id):
        self.in_amount = in_amount
        self.out_amount = out_amount
        self.in_currency_code = in_currency_code
        self.out_currency_code = out_currency_code
        self.mint = mint
        self.user_id = user_id

class Currency(Base):
    """A Currency or unit of account"""
    __name__ = "currency"

    code = sa.Column(sa.String(3), primary_key=True)
    sig_digs = sa.Column(sa.Integer, default=5, nullable=False)

