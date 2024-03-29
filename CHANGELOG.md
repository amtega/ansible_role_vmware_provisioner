# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.8.3] - 2022-07-01
### Fixed
- Remove `latest` requirement for some packages. Related to ansible/playbooks/linux#109 and ansible/roles/amtega.mysql#15
- Coding standards.

## [1.8.2] - 2022-04-28
### Added
- Fixed templating error.

## [1.8.1] - 2022-04-28
### Added
- Fixed templating error.

## [1.8.0] - 2022-04-28
### Added
- Added option to indicate if virtual machines disks should be managed.

## [1.7.3] - 2022-04-28
### Fixed
- Setup direct disk provisioning only for state present7absent. Related to ansible/playbooks/linux#86

## [1.7.2] - 2022-04-27
### Fixed
- Run sequential disk provisioning only for state present. Related to ansible/playbooks/linux#86

## [1.7.1] - 2022-04-27
### Fixed
- Skip direct disk provisioning for templates. Related to ansible/playbooks/linux#86

## [1.7.0] - 2022-04-21
### Changed
- Multiple optimizations.

### Added
- Added new config vars.

## [1.6.1] - 2022-02-22
### Changed
- Adapted for CentOS derived distros. Related to ansible/main#263

## [1.6.0] - 2022-01-26
### Changed
- Supported distros. Related to ansible/main#178

## [1.5.5] - 2022-01-14
### Fixed
- Fixed error verbosity. Related to ansible/roles/amtega.vmware_provisioner#48

## [1.5.4] - 2021-11-29
### Fixed
- Fixed bug with virtual machines wihout disks defined.
