# Method 1: Install Python using pyenv
# Install pyenv dependencies (try with your tmp cache method)
sudo apt -o Dir::Cache::Archives="/tmp/apt-cache" install make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

# Install pyenv
curl https://pyenv.run | bash

# Add to your shell (add to ~/.bashrc)
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc

# Install Python 3.11 (or any version you want)
pyenv install 3.11.0
pyenv global 3.11.0

---
# Method 2: Build python from source

# Download Python source
wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz
tar -xf Python-3.11.0.tgz
cd Python-3.11.0

# Configure and build
./configure --prefix=$HOME/.local --enable-optimizations
make -j4
make altinstall  # altinstall avoids overwriting system python

# Add to PATH
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
