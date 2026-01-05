# TestComplete Package Manager (TPM)

**TestComplete Package Manager (TPM)** is a command-line utility that simplifies how reusable TestComplete assets, utilities, and configurations are distributed and installed into projects. TPM allows you to quickly install prebuilt Test Items and supporting file structures, making advanced automation capabilities available to any TestComplete user in seconds — without requiring extensive knowledge in scripting or expertise in the designing of durable, interdependent file structures.

**TPM** is inspired by package managers like `npm`, but is purpose-built for TestComplete.

> ⚠️ **Early Release Notice**  
> TPM is currently an early-stage, non–feature-complete framework.  
> This release establishes the core architecture and workflow that future versions will build upon.

---

## Installation (Windows)

Download the installer from the official GitHub release:

👉 **[Download TPM v0.1.0 Installer](https://github.com/jdsmartbear/TestComplete-Package-Manager/releases/download/v0.1.0/tpm-setup.exe)**

Run the installer and follow the prompts.  
Administrative privileges are required because TPM installs to `Program Files` and updates the system `PATH`.

After installation, open a **new Command Prompt** and verify:

```bat
tpm -v
```

Expected output:

<pre>
tpm version 0.1.0
</pre>

---

## Basic Usage

TPM commands are executed from a Command Prompt.  
Packages are installed into **the current working directory**.

### Install a package

```bat
tpm install <package-name>
```

Short form:

```bat
tpm i <package-name>
```

Example:

```bat
tpm install placeholder-package
```

---

### List available packages _(framework placeholder)_

```bat
tpm list
```

> Note: In v0.1.0 this command is a stub and will be expanded in future releases.

---

### Uninstall a package _(framework placeholder)_

```bat
tpm uninstall <package-name>
```

> Note: Uninstall behavior is not yet implemented in v0.1.0.

---

### Show version

```bat
tpm -v
```

or

```bat
tpm --version
```

---

## How TPM Works (High-Level)

- Packages are hosted in a centralized GitHub repository
- TPM downloads package contents at install time
- Files are copied directly into the target directory
- No runtime dependencies are required
- No Python installation is required on end-user machines

TPM intentionally avoids:

- implicit dependency graphs
- automatic conflict resolution
- hidden project mutations

---

## Roadmap (Planned)

Future versions will introduce:

- Package metadata (`tpm.json`)
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

TPM modifies files on disk.  
Always review package contents and use version control when integrating TPM into production TestComplete projects.
