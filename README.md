# TestComplete Package Manager (TCPM)

**TestComplete Package Manager (TCPM)** is a command-line utility that simplifies how reusable TestComplete assets, utilities, and configurations are distributed and installed into projects. TCPM allows you to quickly install prebuilt Test Items and supporting file structures, making advanced automation capabilities available to any TestComplete user in seconds — without requiring extensive knowledge in scripting or expertise in the designing of durable, interdependent file structures.

**TCPM** is inspired by package managers like `npm`, but is purpose-built for TestComplete.

> ⚠️ **Early Release Notice**  
> TCPM is currently an early-stage, non–feature-complete framework.  
> This release establishes the core architecture and workflow that future versions will build upon.

---

## Installation (Windows)

Download the installer from the official GitHub release:

👉 **[Download TCPM v0.1.0 Installer](https://github.com/jdsmartbear/TestComplete-Package-Manager/releases/download/v0.1.0/tcpm-setup.exe)**

Run the installer and follow the prompts.  
Administrative privileges are required because TCPM installs to `Program Files` and updates the system `PATH`.

After installation, open a **new Command Prompt** and verify:

```bat
tcpm -v
```

Expected output:

<pre>
tcpm version 0.1.0
</pre>

---

## Basic Usage

TCPM commands are executed from a Command Prompt.  
Packages are installed into **the current working directory**.

### Install a package

```bat
tcpm install <package-name>
```

Short form:

```bat
tcpm i <package-name>
```

Example:

```bat
tcpm install placeholder-package
```

---

### List available packages _(framework placeholder)_

```bat
tcpm list
```

> Note: In v0.1.0 this command is a stub and will be expanded in future releases.

---

### Uninstall a package _(framework placeholder)_

```bat
tcpm uninstall <package-name>
```

> Note: Uninstall behavior is not yet implemented in v0.1.0.

---

### Show version

```bat
tcpm -v
```

or

```bat
tcpm --version
```

---

## How TCPM Works (High-Level)

- Packages are hosted in a centralized GitHub repository
- TCPM downloads package contents at install time
- Files are copied directly into the target directory
- No runtime dependencies are required
- No Python installation is required on end-user machines

TCPM intentionally avoids:

- implicit dependency graphs
- automatic conflict resolution
- hidden project mutations

---

## Roadmap (Planned)

Future versions will introduce:

- Package metadata (`tcpm.json`)
- Safer uninstall behavior
- Installation tracking
- Dry-run mode
- Per-user (non-admin) installation option
- Additional built-in packages

---

## License

MIT License

---

## Disclaimer

TCPM modifies files on disk.  
Always review package contents and use version control when integrating TCPM into production TestComplete projects.
