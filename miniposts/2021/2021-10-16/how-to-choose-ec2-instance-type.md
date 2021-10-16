# How to choose EC2 instance type

- if single core performance is most important, choose from c5, m6i, m5zn
- if the instance will be idle most of the time, choose between t3, t3a, t4g
- if arm server can be used, choose between c6g, m6g, r6g
- otherwise consider using m6i, c5, c5a; r5, r5a if more memory needed
- test your workload on different instance types to be sure
