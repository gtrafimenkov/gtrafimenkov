# Tripping on eventual consistency

There are many things in AWS that can trip you up, one of them is
eventual consistency.

I was setting up GuardDuty.  A pretty simple configuration it was:
- a GuardDuty detector
- a CloudWatch Events rule
- an SNS topic to send findings to

I deployed it with Terraform, subscribed myself to the SNS topic,
went to the GuardDuty settings and pressed a button to generate
sample findings.

A few minutes went by, no messages from the SNS topic.  "There must be
a problem with CloudWatch Events rule", I thought and went checking it,
SNS topic IAM policy, and everything.

After a couple of hours of checking, rechecking, configuring manually
and comparing with the results of Terraform deploy, looking at metrics,
going through CloudTrail logs for signs of possible permissions errors,
etc, I found a problem.

Everything was fine with my initial configuration.  I just sent sample
findings too fast and they didn't make it through the internal machinery
of AWS all the way to the SNS subscription.

AWS is eventually consistent, sometimes it takes time to connect all
the necessary pipes and dots together.
