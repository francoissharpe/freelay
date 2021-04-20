from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field


class CloudMailInHeaders(BaseModel):
    received: List[str]
    date: str
    from_address: str = Field(..., alias="from")
    to_address: str = Field(..., alias="to")
    message_id: str
    subject: str
    mime_version: str
    content_type: str
    arc_authentication_results: str


class CloudMailInEnvelope(BaseModel):
    from_address: str = Field(..., alias="from")
    to_address: str = Field(..., alias="to")
    recipients: List[str]
    remote_ip: str


class CloudMailIn(BaseModel):
    # headers: CloudMailInHeaders
    envelope: CloudMailInEnvelope
    plain: str
    html: str
#     {
#   "envelope": {
#     "to": "to@example.com",
#     "from": "from@example.com",
#     "helo_domain": "localhost",
#     "remote_ip": "127.0.0.1",
#     "recipients": [
#       "to@example.com",
#       "another@example.com"
#     ],
#     "spf": {
#       "result": "pass",
#       "domain": "example.com"
#     },
#     "tls": true,
#   },
#   "plain": "Test with HTML.",
#   "html": "<html><head>\n<meta http-equiv=\"content-type\" content=\"text/html; charset=ISO-8859-1\"></head><body\n bgcolor=\"#FFFFFF\" text=\"#000000\">\nTest with <span style=\"font-weight: bold;\">HTML</span>.<br>\n</body>\n</html>",
#   "reply_plain": "Message reply if found.",
#   "attachments": [
#     {
#       "content": "dGVzdGZpbGU=",
#       "file_name": "file.txt",
#       "content_type": "text/plain",
#       "size": 8,
#       "disposition": "attachment"
#     },
#     {
#       "content": "dGVzdGZpbGU=",
#       "file_name": "file.txt",
#       "content_type": "text/plain",
#       "size": 8,
#       "disposition": "attachment"
#     }
#   ]
# }


# class EmailCreate(EmailBase):
#     pass


# class Email(EmailBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True


# class UserBase(BaseModel):
#     email: str


# class UserCreate(UserBase):
#     password: str


# class User(UserBase):
#     id: int
#     is_active: bool
#     generated_emails: List[Email]

#     class Config:
#         orm_mode = True
