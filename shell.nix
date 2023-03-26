{ pkgs ? import <nixpkgs> {}}:
  pkgs.mkShell {
    nativeBuildInputs = let
      env = pyPkgs : with pyPkgs; [
        selenium
      ];
    in with pkgs; [
      (python39.withPackages env)
      pkgs.chromedriver
      pkgs.chromium
      (pkgs.writeShellScriptBin "google-chrome" "exec -a $0 ${pkgs.chromium}/bin/chromium $@")
    ];
}
