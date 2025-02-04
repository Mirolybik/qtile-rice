#!/bin/sh

if [ -d ~/.config/rofi ]; then
  mv -v ~/.config/rofi ~/.config/rofi-old
fi

if [ -d ~/.config/qtile ]; then
  mv -v ~/.config/qtile ~/.config/qtile-old
fi

if [ -d ~/.config/kitty ]; then
  mv -v ~/.config/kitty ~/.config/kitty-old
fi

if [ -d ~/.config/nvim]; then
  mv -v ~/.config/nvim ~/.config/nvim-old
fi

if [ -d ~/.config/dunst ]; then
  mv -v ~/.config/dunst ~/.config/dunst-old
fi

if [ -f ~/.Xresources ]; then
  mv -v ~/.Xresources ~/.Xresources.old
fi

if [ -f ~/.zshrc]; then
  mv -v ~/.zshrc ~/.zshrc.old
fi


cp -rv ./config/* ~/.config
cp -v .Xresources ~/
