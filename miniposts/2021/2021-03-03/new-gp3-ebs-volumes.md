# New gp3 EBS volumes

AWS recently [announced](https://aws.amazon.com/about-aws/whats-new/2020/12/introducing-new-amazon-ebs-general-purpose-volumes-gp3/) new general purpose
EBS volumes - gp3, which are more performant and cheaper that the previous
generation (gp2).

gp3 provides better performance over gp2 for any volume of less 1000 GB in size.

Here is the math:
- gp3 by default provides 3000 IOPS of consistent performance regardless of the volume size
- gp2 provides `max(100, 3*volume_size_in_gb)` IOPS plus a temporary boost up 3000 IOPS

Regarding the pricing:
- in us-east-1 region gp3 is $0.08/GB-month, gp2 is $0.10/GB-month; gp3 is 20% cheaper
- in eu-west-1 region gp3 is $0.0952/GB-month, gp2 is $0.1190/GB-month; gp3 is 20% cheaper again

Terraform already supports the new volume type.

## Conclusions

- use gp3 instead of gp2 for any volume of less than 1000GB in size
- if you overprovisioned gp2 volumes before to achieve better performance,
  consider moving to gp3 and reducing the volume size
- for volumes bigger than 1000GB, analyze IOPS and bandwidth consumption
  by your application and decide what volume type will be better on case by
  case basis; also consider other volume types

## Links

- https://aws.amazon.com/about-aws/whats-new/2020/12/introducing-new-amazon-ebs-general-purpose-volumes-gp3/
- https://aws.amazon.com/ebs/pricing/
- https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ebs_volume
