# Go Tutorial: Getting started with multi-module workspaces

Source: [Tutorial: Getting started with multi-module workspaces](https://go.dev/doc/tutorial/workspaces)

## Usage

Run from hello directory:

```text
.../multi-module_workspaces/workspace/hello $ go run example.com/hello
HELLO
```

Run from parent workspace directory:

```text
.../multi-module_workspaces/workspace $ go run example.com/hello
HELLO
```
