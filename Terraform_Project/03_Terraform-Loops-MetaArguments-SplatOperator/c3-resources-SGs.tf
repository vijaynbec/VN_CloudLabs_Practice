
# Creating Security Group SSH Traffic
resource "aws_security_group" "allow_ssh" {
  name        = "allow_ssh"
  description = "Allow ssh inbound traffic and all outbound traffic"

  ingress {
    description = "allow ssh rule for inbound port 22"
    from_port = 22
    protocol  = "tcp"
    to_port   = 22
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    description = "allow outbond"
    from_port = 0
    protocol  = "-1"
    to_port   = 0
  }
  tags = {
    Name = "allow_sg-ssh"
  }
}


# Creating Security Group WEB Traffic
resource "aws_security_group" "allow_web" {
  name        = "allow_web"
  description = "Allow web inbound traffic and all outbound traffic"

  ingress {
    description = "allow web rule for inbound port 80"
    from_port = 80
    protocol  = "tcp"
    to_port   = 80
    cidr_blocks = ["0.0.0.0/0"]
  }
    ingress {
    description = "allow web rule for inbound port 443"
    from_port = 443
    protocol  = "tcp"
    to_port   = 443
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    description = "allow outbond"
    from_port = 0
    protocol  = "-1"
    to_port   = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "allow_sg-web"
  }
}


/* we can defined the ingress and egress rule as below as well
resource "aws_vpc_security_group_ingress_rule" "allow_ssh_ipv4" {
  security_group_id = aws_security_group.allow_ssh.id
  cidr_ipv4         = ["0.0.0.0/0"]
  from_port         = 22
  ip_protocol       = "tcp"
  to_port           = 22
}

resource "aws_vpc_security_group_egress_rule" "allow_all_egress" {
  security_group_id = aws_security_group.allow_ssh.id
  cidr_ipv4         = ["0.0.0.0/0"]
  from_port         = 0
  ip_protocol       = "-1"
  to_port           = 0
}
*/