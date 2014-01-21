# base-minimal

Collections of mostly header-only utility classes from Chromium's base library,
just add `base.gyp:base` to your gyp file to use them.

##Usage

**Install gyp**
```bash
git clone https://chromium.googlesource.com/external/gyp.git
export PATH=$PATH:$your_gyp_path
```

**Generate sample project files**
```bash
gyp --depth=. hello.gyp
```

**Build with ninja**
```bash
ninja -C out/Default hello
```
