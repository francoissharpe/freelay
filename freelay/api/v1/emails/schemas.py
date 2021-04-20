from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field


class CloudMailInHeaders(BaseModel):
    return_path: str = Field(..., alias="Return-Path")
    received: List[str] = Field(..., alias="Received")
    date: str = Field(..., alias="Date")
    from_address: str = Field(..., alias="From")
    to_address: str = Field(..., alias="To")
    message_id: str = Field(..., alias="Message-ID")
    subject: str = Field(..., alias="Subject")
    mime_version: str = Field(..., alias="Mime-Version")
    content_type: str = Field(..., alias="Content-Type")
    delivered_to: str = Field(..., alias="Delivered-To")
    received_spf: str = Field(..., alias="Received-SPF")
    authentication_results: str = Field(..., alias="Authentication-Results")
    user_agent: str = Field(..., alias="User-Agent")


# class CloudMailInEnvelope(BaseModel):
#     to_address: str = Field(..., alias="Return-Path")
#     received: List[str] = Field(..., alias="Received")
#     date: str = Field(..., alias="Date")
#     from_address: str = Field(..., alias="From")
#     to_address: str = Field(..., alias="To")
#     message_id: str = Field(..., alias="Message-ID")
#     subject: str = Field(..., alias="Subject")
#     mime_version: str = Field(..., alias="Mime-Version")
#     content_type: str = Field(..., alias="Content-Type")
#     delivered_to: str = Field(..., alias="Delivered-To")
#     received_spf: str = Field(..., alias="Received-SPF")
#     authentication_results: str = Field(..., alias="Authentication-Results")
#     user_agent: str = Field(..., alias="User-Agent")


class CloudMailIn(BaseModel):
    headers: CloudMailInHeaders
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
