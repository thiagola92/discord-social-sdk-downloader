FROM fedora:43
USER root

WORKDIR /workspace

# Install prerequisites for container
RUN dnf install -y uv

# Install prerequisites for GDExtension.
RUN dnf install -y python3-scons
RUN dnf install -y libstdc++-static
RUN dnf install -y clang
RUN dnf install -y clang-tools-extra
RUN dnf install -y doxygen
RUN dnf install -y mingw64-gcc-c++

# Download Godot 4.4.
RUN curl -L -o godot.zip "https://downloads.godotengine.org/?version=4.4&flavor=stable&slug=linux.x86_64.zip&platform=linux.64"
RUN unzip godot.zip
RUN rm godot.zip
RUN mv Godot_v* godot

# Setup SDK downloader.
COPY .python-version main.py pyproject.toml uv.lock version discord-social-sdk-downloader/
RUN uv python install 3.13
RUN cd discord-social-sdk-downloader && uv sync

# Don't stop container.
CMD ["sleep", "infinity"]
