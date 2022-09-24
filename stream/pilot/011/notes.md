# Pilot Stream 011 Notes

## Summary

The one where I revisit the [health_checker](https://github.com/conflabermits/health_checker) project and try to make it release-ready!

## Details

Right now the project is kinda broken. I ported it over to its own repo and started trying to separate the logic into a separate file that can be used by both the CLI program and the web program. It still needs some attention before it works the way I'm hoping.

```bash
$ go run main.go -help
package command-line-arguments
	imports github.com/conflabermits/health_checker/hcfunc
	imports github.com/conflabermits/health_checker/hcfunc: import cycle not allowed
```

```bash
$ go run web.go -help
# command-line-arguments
runtime.main_main·f: function main is undeclared in the main package
```

## References

* [health_checker](https://github.com/conflabermits/health_checker) repo
