# Finding info in files

Using `grep`

- -A<n> = list <n> after <target info>
- -B<n> = list <n> before <target info>
- -C<n> = list <n> both after & before <target info>

<tools> -h or --help | grep <target info> -A<n> or -B<n>

Example:

```sh
nmap -h | grep OUTPUT -A10
```

```sh
mysql --help | grep OUTPUT -A10
```
