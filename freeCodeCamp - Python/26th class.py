# networked programs

# transport control protocol (tcp)
# built on top of IP (internet protocol). Assumes IP might lose some data - stores
# and retransmits data if it seems to be lost.
# Handles "flow control" using a transmit window.
# Provides a nice reliable pipe

# tcp connections / sockets
# in computer networking, and internet socket or network socket is an endpoint
# of a bidirectional inter-process communication flow across an internet
# Protocol-based computer network, such as the internet

# a port is an application-specific or process-specific software communications
# endpoint. It allows multiple networked applications to coexist on the same server.
# There is a list of well-known TCP port numbers

# common tcp ports:
# telnet (23) - Login
# SSH (22) - Secure Login
# HTTP (80)
# HTTPS (443) - Secure
# SMTP (25) - (MAIL)
# IMAP (143/220/993) - Mail Retrieval
# POP (109/110) - Mail Retrieavel
# DNS (53) - Domain Name
# FTP (21) - File Transfer

# sometimes we see the tcp port, that means that is a non-official

# sockets in python
# python has a built-in support for TCP sockets

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

print(mysock)

# application protocols

