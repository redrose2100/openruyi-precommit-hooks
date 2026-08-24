# check-spec-summary 扫描结果

对 [openRuyi-Project/openRuyi](https://github.com/openRuyi-Project/openRuyi)
仓库的 spec 文件（`SPECS/{pkg}/{pkg}.spec`，默认分支 `master`）执行
`check-spec-summary` 规则的扫描结果。

## 结果概览

| 项目 | 数量 |
| --- | --- |
| 扫描 spec 文件总数 | 5337 |
| 通过 | 5224 |
| 违规数量 | 113 |

## 分布统计

| Summary 写法类别 | 数量 |
| --- | --- |
| 正常（简短英文描述，不以句号结尾） | 5224 |
| 以英文句号 `.` 结尾 | 113 |
| 含 CJK / 全角字符（非英文介绍） | 0 |
| 含宏展开（如 `%{name}`、`%{pkg_desc}`） | 8（跳过判定） |
| 缺失 / 空 `Summary` 字段 | 0 |

## 违规清单（113 条）

| spec 文件 | Summary 值 | 违规类型 |
| --- | --- | --- |
| [Xwayland/Xwayland.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/Xwayland/Xwayland.spec) | `Xwayland is an X server for running X clients under Wayland.` | 以英文句号 `.` 结尾 |
| [autofs/autofs.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/autofs/autofs.spec) | `A tool from automatically mounting and umounting filesyst...` | 以英文句号 `.` 结尾 |
| [dblatex/dblatex.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/dblatex/dblatex.spec) | `A LaTeX-based converter for transforming DocBook XML and ...` | 以英文句号 `.` 结尾 |
| [go-aead-dev-mem/go-aead-dev-mem.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-aead-dev-mem/go-aead-dev-mem.spec) | `The mem package provides types and functions for measurin...` | 以英文句号 `.` 结尾 |
| [go-aead-dev-minisign/go-aead-dev-minisign.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-aead-dev-minisign/go-aead-dev-minisign.spec) | `A dead simple tool to sign files and verify digital signa...` | 以英文句号 `.` 结尾 |
| [go-aead-dev-mtls/go-aead-dev-mtls.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-aead-dev-mtls/go-aead-dev-mtls.spec) | `A Go library for TLS/HTTPS using public key pinning inste...` | 以英文句号 `.` 结尾 |
| [go-filippo-edwards25519/go-filippo-edwards25519.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-filippo-edwards25519/go-filippo-edwards25519.spec) | `filippo.io/edwards25519 — A safer, faster, and more power...` | 以英文句号 `.` 结尾 |
| [go-github-agext-levenshtein/go-github-agext-levenshtein.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-agext-levenshtein/go-github-agext-levenshtein.spec) | `Levenshtein distance and similarity metrics with customiz...` | 以英文句号 `.` 结尾 |
| [go-github-agnivade-levenshtein/go-github-agnivade-levenshtein.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-agnivade-levenshtein/go-github-agnivade-levenshtein.spec) | `Go implementation to calculate Levenshtein Distance.` | 以英文句号 `.` 结尾 |
| [go-github-anmitsu-go-shlex/go-github-anmitsu-go-shlex.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-anmitsu-go-shlex/go-github-anmitsu-go-shlex.spec) | `A library to make a lexical analyzer like Unix shell for ...` | 以英文句号 `.` 结尾 |
| [go-github-apache-beam/go-github-apache-beam.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-apache-beam/go-github-apache-beam.spec) | `Apache Beam is a unified programming model for Batch and ...` | 以英文句号 `.` 结尾 |
| [go-github-aperturerobotics-protobuf-go-lite/go-github-aperturerobotics-protobuf-go-lite.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-aperturerobotics-protobuf-go-lite/go-github-aperturerobotics-protobuf-go-lite.spec) | `Reflection-free Protobuf for Go.` | 以英文句号 `.` 结尾 |
| [go-github-aymanbagabas-go-osc52/go-github-aymanbagabas-go-osc52.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-aymanbagabas-go-osc52/go-github-aymanbagabas-go-osc52.spec) | `Golang terminal ANSI OSC52 wrapper. Copy text to clipboar...` | 以英文句号 `.` 结尾 |
| [go-github-bahlo-generic-list-go/go-github-bahlo-generic-list-go.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-bahlo-generic-list-go/go-github-bahlo-generic-list-go.spec) | `Go container/list but with generics.` | 以英文句号 `.` 结尾 |
| [go-github-benmathews-bench/go-github-benmathews-bench.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-benmathews-bench/go-github-benmathews-bench.spec) | `A generic latency benchmarking library.` | 以英文句号 `.` 结尾 |
| [go-github-boltdb-bolt/go-github-boltdb-bolt.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-boltdb-bolt/go-github-boltdb-bolt.spec) | `An embedded key/value database for Go.` | 以英文句号 `.` 结尾 |
| [go-github-chzyer-test/go-github-chzyer-test.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-chzyer-test/go-github-chzyer-test.spec) | `A Go library designed to enhance testing capabilities.` | 以英文句号 `.` 结尾 |
| [go-github-clipperhouse-uax29-v2/go-github-clipperhouse-uax29-v2.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-clipperhouse-uax29-v2/go-github-clipperhouse-uax29-v2.spec) | `A tokenizer based on Unicode text segmentation (UAX #29),...` | 以英文句号 `.` 结尾 |
| [go-github-code-hex-go-generics-cache/go-github-code-hex-go-generics-cache.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-code-hex-go-generics-cache/go-github-code-hex-go-generics-cache.spec) | `A key:value store/cache library written in Go generics. L...` | 以英文句号 `.` 结尾 |
| [go-github-coreos-go-oidc/go-github-coreos-go-oidc.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-coreos-go-oidc/go-github-coreos-go-oidc.spec) | `A Go OpenID Connect client.` | 以英文句号 `.` 结尾 |
| [go-github-cosiner-argv/go-github-cosiner-argv.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-cosiner-argv/go-github-cosiner-argv.spec) | `A library for Go to split command line string into argume...` | 以英文句号 `.` 结尾 |
| [go-github-dchest-siphash/go-github-dchest-siphash.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-dchest-siphash/go-github-dchest-siphash.spec) | `Go implementation of SipHash-2-4, a fast short-input PRF ...` | 以英文句号 `.` 结尾 |
| [go-github-etcd-io-bbolt/go-github-etcd-io-bbolt.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-etcd-io-bbolt/go-github-etcd-io-bbolt.spec) | `An embedded key/value database for Go.` | 以英文句号 `.` 结尾 |
| [go-github-felixge-fgprof/go-github-felixge-fgprof.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-felixge-fgprof/go-github-felixge-fgprof.spec) | `🚀 fgprof is a sampling Go profiler that allows you to ana...` | 以英文句号 `.` 结尾 |
| [go-github-fsnotify-fsnotify/go-github-fsnotify-fsnotify.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-fsnotify-fsnotify/go-github-fsnotify-fsnotify.spec) | `Cross-platform filesystem notifications for Go.` | 以英文句号 `.` 结尾 |
| [go-github-gin-contrib-sse/go-github-gin-contrib-sse.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-gin-contrib-sse/go-github-gin-contrib-sse.spec) | `Server-Sent Events implementation in Go. Used by the Gin ...` | 以英文句号 `.` 结尾 |
| [go-github-gin-gonic-gin/go-github-gin-gonic-gin.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-gin-gonic-gin/go-github-gin-gonic-gin.spec) | `Gin is a high-performance HTTP web framework written in G...` | 以英文句号 `.` 结尾 |
| [go-github-go-ldap-ldap/go-github-go-ldap-ldap.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-go-ldap-ldap/go-github-go-ldap-ldap.spec) | `Basic LDAP v3 functionality for the GO programming language.` | 以英文句号 `.` 结尾 |
| [go-github-go-logfmt-logfmt/go-github-go-logfmt-logfmt.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-go-logfmt-logfmt/go-github-go-logfmt-logfmt.spec) | `Package logfmt marshals and unmarshals logfmt messages.` | 以英文句号 `.` 结尾 |
| [go-github-go-viper-mapstructure-v2/go-github-go-viper-mapstructure-v2.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-go-viper-mapstructure-v2/go-github-go-viper-mapstructure-v2.spec) | `Go library for decoding generic map values into native Go...` | 以英文句号 `.` 结尾 |
| [go-github-gobwas-httphead/go-github-gobwas-httphead.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-gobwas-httphead/go-github-gobwas-httphead.spec) | `Tiny HTTP header value parsing library in go.` | 以英文句号 `.` 结尾 |
| [go-github-gobwas-ws/go-github-gobwas-ws.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-gobwas-ws/go-github-gobwas-ws.spec) | `Tiny WebSocket library for Go.` | 以英文句号 `.` 结尾 |
| [go-github-golang-jwt-jwt-v5/go-github-golang-jwt-jwt-v5.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-golang-jwt-jwt-v5/go-github-golang-jwt-jwt-v5.spec) | `Go implementation of JSON Web Tokens (JWT).` | 以英文句号 `.` 结尾 |
| [go-github-golang-snappy/go-github-golang-snappy.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-golang-snappy/go-github-golang-snappy.spec) | `The Snappy compression format in the Go programming langu...` | 以英文句号 `.` 结尾 |
| [go-github-google-btree/go-github-google-btree.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-google-btree/go-github-google-btree.spec) | `BTree provides a simple, ordered, in-memory data structur...` | 以英文句号 `.` 结尾 |
| [go-github-google-gofuzz/go-github-google-gofuzz.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-google-gofuzz/go-github-google-gofuzz.spec) | `Fuzz testing for go.` | 以英文句号 `.` 结尾 |
| [go-github-google-licensecheck/go-github-google-licensecheck.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-google-licensecheck/go-github-google-licensecheck.spec) | `The licensecheck package classifies license files and heu...` | 以英文句号 `.` 结尾 |
| [go-github-google-uuid/go-github-google-uuid.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-google-uuid/go-github-google-uuid.spec) | `Go package for UUIDs based on RFC 4122 and DCE 1.1: Authe...` | 以英文句号 `.` 结尾 |
| [go-github-gookit-color/go-github-gookit-color.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-gookit-color/go-github-gookit-color.spec) | `A command-line color library with 16/256/True color suppo...` | 以英文句号 `.` 结尾 |
| [go-github-gorilla-websocket/go-github-gorilla-websocket.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-gorilla-websocket/go-github-gorilla-websocket.spec) | `Package gorilla/websocket is a fast, well-tested and wide...` | 以英文句号 `.` 结尾 |
| [go-github-hashicorp-errwrap/go-github-hashicorp-errwrap.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-hashicorp-errwrap/go-github-hashicorp-errwrap.spec) | `Errwrap is a Go (golang) library for wrapping and queryin...` | 以英文句号 `.` 结尾 |
| [go-github-hashicorp-go-checkpoint/go-github-hashicorp-go-checkpoint.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-hashicorp-go-checkpoint/go-github-hashicorp-go-checkpoint.spec) | `Checkpoint is an internal service at Hashicorp that we us...` | 以英文句号 `.` 结尾 |
| [go-github-hashicorp-go-connlimit/go-github-hashicorp-go-connlimit.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-hashicorp-go-connlimit/go-github-hashicorp-go-connlimit.spec) | `A simple library that allows a network server to limit ho...` | 以英文句号 `.` 结尾 |
| [go-github-hashicorp-go-multierror/go-github-hashicorp-go-multierror.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-hashicorp-go-multierror/go-github-hashicorp-go-multierror.spec) | `A Go (golang) package for representing a list of errors a...` | 以英文句号 `.` 结尾 |
| [go-github-hashicorp-go-rootcerts/go-github-hashicorp-go-rootcerts.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-hashicorp-go-rootcerts/go-github-hashicorp-go-rootcerts.spec) | `Functions for loading root certificates for TLS connections.` | 以英文句号 `.` 结尾 |
| [go-github-hashicorp-go-version/go-github-hashicorp-go-version.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-hashicorp-go-version/go-github-hashicorp-go-version.spec) | `A Go (golang) library for parsing and verifying versions ...` | 以英文句号 `.` 结尾 |
| [go-github-hashicorp-hil/go-github-hashicorp-hil.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-hashicorp-hil/go-github-hashicorp-hil.spec) | `HIL is a small embedded language for string interpolations.` | 以英文句号 `.` 结尾 |
| [go-github-hashicorp-terraform-plugin-log/go-github-hashicorp-terraform-plugin-log.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-hashicorp-terraform-plugin-log/go-github-hashicorp-terraform-plugin-log.spec) | `Module for logging from Terraform plugins.` | 以英文句号 `.` 结尾 |
| [go-github-hashicorp-vic/go-github-hashicorp-vic.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-hashicorp-vic/go-github-hashicorp-vic.spec) | `vSphere Integrated Containers Engine is a container runti...` | 以英文句号 `.` 结尾 |
| [go-github-kataras-golog/go-github-kataras-golog.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-kataras-golog/go-github-kataras-golog.spec) | `A high-performant Logging Foundation for Go Applications....` | 以英文句号 `.` 结尾 |
| [go-github-kr-fs/go-github-kr-fs.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-kr-fs/go-github-kr-fs.spec) | `Package fs provides filesystem-related functions.` | 以英文句号 `.` 结尾 |
| [go-github-lesismal-llib/go-github-lesismal-llib.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-lesismal-llib/go-github-lesismal-llib.spec) | `llib - nbio's dependency lib.` | 以英文句号 `.` 结尾 |
| [go-github-lesismal-nbio/go-github-lesismal-nbio.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-lesismal-nbio/go-github-lesismal-nbio.spec) | `Pure Go 1000k+ connections solution, support tls/http1.x/...` | 以英文句号 `.` 结尾 |
| [go-github-lucasb-eyer-go-colorful/go-github-lucasb-eyer-go-colorful.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-lucasb-eyer-go-colorful/go-github-lucasb-eyer-go-colorful.spec) | `A library for playing with colors in go (golang).` | 以英文句号 `.` 结尾 |
| [go-github-mailru-easyjson/go-github-mailru-easyjson.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-mailru-easyjson/go-github-mailru-easyjson.spec) | `Fast JSON serializer for golang.` | 以英文句号 `.` 结尾 |
| [go-github-minio-csvparser/go-github-minio-csvparser.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-minio-csvparser/go-github-minio-csvparser.spec) | `Package csv reads and writes comma-separated values (CSV)...` | 以英文句号 `.` 结尾 |
| [go-github-minio-sio/go-github-minio-sio.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-minio-sio/go-github-minio-sio.spec) | `Go implementation of the Data At Rest Encryption (DARE) f...` | 以英文句号 `.` 结尾 |
| [go-github-minio-websocket/go-github-minio-websocket.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-minio-websocket/go-github-minio-websocket.spec) | `A fast, well-tested and widely used WebSocket implementat...` | 以英文句号 `.` 结尾 |
| [go-github-minio-xxml/go-github-minio-xxml.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-minio-xxml/go-github-minio-xxml.spec) | `Package xml implements a simple XML 1.0 parser that under...` | 以英文句号 `.` 结尾 |
| [go-github-mitchellh-colorstring/go-github-mitchellh-colorstring.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-mitchellh-colorstring/go-github-mitchellh-colorstring.spec) | `Go (golang) library for colorizing strings for terminal o...` | 以英文句号 `.` 结尾 |
| [go-github-mitchellh-copystructure/go-github-mitchellh-copystructure.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-mitchellh-copystructure/go-github-mitchellh-copystructure.spec) | `Go (golang) library for deep copying values in Go.` | 以英文句号 `.` 结尾 |
| [go-github-mitchellh-go-homedir/go-github-mitchellh-go-homedir.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-mitchellh-go-homedir/go-github-mitchellh-go-homedir.spec) | `Go library for detecting and expanding the user's home di...` | 以英文句号 `.` 结尾 |
| [go-github-mitchellh-go-ps/go-github-mitchellh-go-ps.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-mitchellh-go-ps/go-github-mitchellh-go-ps.spec) | `Find, list, and inspect processes from Go (golang).` | 以英文句号 `.` 结尾 |
| [go-github-mitchellh-go-testing-interface/go-github-mitchellh-go-testing-interface.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-mitchellh-go-testing-interface/go-github-mitchellh-go-testing-interface.spec) | `Go (golang) library to expose *testing.T as an interface.` | 以英文句号 `.` 结尾 |
| [go-github-mitchellh-go-wordwrap/go-github-mitchellh-go-wordwrap.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-mitchellh-go-wordwrap/go-github-mitchellh-go-wordwrap.spec) | `A Go (golang) library for wrapping words in a string.` | 以英文句号 `.` 结尾 |
| [go-github-mitchellh-hashstructure/go-github-mitchellh-hashstructure.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-mitchellh-hashstructure/go-github-mitchellh-hashstructure.spec) | `Get hash values for arbitrary values in Go (golang).` | 以英文句号 `.` 结尾 |
| [go-github-mitchellh-mapstructure/go-github-mitchellh-mapstructure.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-mitchellh-mapstructure/go-github-mitchellh-mapstructure.spec) | `Go library for decoding generic map values into native Go...` | 以英文句号 `.` 结尾 |
| [go-github-mitchellh-pointerstructure/go-github-mitchellh-pointerstructure.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-mitchellh-pointerstructure/go-github-mitchellh-pointerstructure.spec) | `Go library for addressing and reading/writing a specific ...` | 以英文句号 `.` 结尾 |
| [go-github-mitchellh-reflectwalk/go-github-mitchellh-reflectwalk.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-mitchellh-reflectwalk/go-github-mitchellh-reflectwalk.spec) | `reflectwalk is a Go library for "walking" complex structu...` | 以英文句号 `.` 结尾 |
| [go-github-munnerz-goautoneg/go-github-munnerz-goautoneg.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-munnerz-goautoneg/go-github-munnerz-goautoneg.spec) | `HTTP Content-Type Autonegotiation.` | 以英文句号 `.` 结尾 |
| [go-github-nlpodyssey-gopickle/go-github-nlpodyssey-gopickle.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-nlpodyssey-gopickle/go-github-nlpodyssey-gopickle.spec) | `Go library for loading Python's data serialized with pick...` | 以英文句号 `.` 结尾 |
| [go-github-olekukonko-cat/go-github-olekukonko-cat.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-olekukonko-cat/go-github-olekukonko-cat.spec) | `cat - Because life's too short for ugly string building c...` | 以英文句号 `.` 结尾 |
| [go-github-oneofone-xxhash/go-github-oneofone-xxhash.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-oneofone-xxhash/go-github-oneofone-xxhash.spec) | `A native implementation of the excellent XXHash hashing a...` | 以英文句号 `.` 结尾 |
| [go-github-prometheus-client-model/go-github-prometheus-client-model.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-prometheus-client-model/go-github-prometheus-client-model.spec) | `Data model artifacts for Prometheus.` | 以英文句号 `.` 结尾 |
| [go-github-prometheus-common/go-github-prometheus-common.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-prometheus-common/go-github-prometheus-common.spec) | `Go libraries shared across Prometheus components and libr...` | 以英文句号 `.` 结尾 |
| [go-github-prometheus-procfs/go-github-prometheus-procfs.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-prometheus-procfs/go-github-prometheus-procfs.spec) | `procfs provides functions to retrieve system, kernel and ...` | 以英文句号 `.` 结尾 |
| [go-github-rabbitmq-amqp091-go/go-github-rabbitmq-amqp091-go.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-rabbitmq-amqp091-go/go-github-rabbitmq-amqp091-go.spec) | `An AMQP 0-9-1 Go client maintained by the RabbitMQ team.` | 以英文句号 `.` 结尾 |
| [go-github-rjeczalik-notify/go-github-rjeczalik-notify.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-rjeczalik-notify/go-github-rjeczalik-notify.spec) | `File system event notification library on steroids.` | 以英文句号 `.` 结尾 |
| [go-github-sanity-io-litter/go-github-sanity-io-litter.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-sanity-io-litter/go-github-sanity-io-litter.spec) | `Litter is a pretty printer library for Go data structures...` | 以英文句号 `.` 结尾 |
| [go-github-spdx-gordf/go-github-spdx-gordf.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-spdx-gordf/go-github-spdx-gordf.spec) | `gordf is a package which provides a parser for RDF files ...` | 以英文句号 `.` 结尾 |
| [go-github-spf13-pflag/go-github-spf13-pflag.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-spf13-pflag/go-github-spf13-pflag.spec) | `Drop-in replacement for Go's flag package, implementing P...` | 以英文句号 `.` 结尾 |
| [go-github-stretchr-objx/go-github-stretchr-objx.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-stretchr-objx/go-github-stretchr-objx.spec) | `Go package for dealing with maps, slices, JSON and other ...` | 以英文句号 `.` 结尾 |
| [go-github-subosito-gotenv/go-github-subosito-gotenv.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-subosito-gotenv/go-github-subosito-gotenv.spec) | `Load environment variables from .env or io.Reader in Go.` | 以英文句号 `.` 结尾 |
| [go-github-ugorji-go-codec/go-github-ugorji-go-codec.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-ugorji-go-codec/go-github-ugorji-go-codec.spec) | `idiomatic codec and rpc lib for msgpack, cbor, json, etc.` | 以英文句号 `.` 结尾 |
| [go-github-wcharczuk-go-chart/go-github-wcharczuk-go-chart.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-wcharczuk-go-chart/go-github-wcharczuk-go-chart.spec) | `go chart is a basic charting library in go.` | 以英文句号 `.` 结尾 |
| [go-github-xrash-smetrics/go-github-xrash-smetrics.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-xrash-smetrics/go-github-xrash-smetrics.spec) | `String metrics library written in Go.` | 以英文句号 `.` 结尾 |
| [go-github-yuin-goldmark/go-github-yuin-goldmark.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-yuin-goldmark/go-github-yuin-goldmark.spec) | `A markdown parser written in Go. Easy to extend, standard...` | 以英文句号 `.` 结尾 |
| [go-github-zeebo-assert/go-github-zeebo-assert.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-github-zeebo-assert/go-github-zeebo-assert.spec) | `Helpers for tests. You don't have to like it.` | 以英文句号 `.` 结尾 |
| [go-gonum-v1-gonum/go-gonum-v1-gonum.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-gonum-v1-gonum/go-gonum-v1-gonum.spec) | `Gonum is a set of numeric libraries for the Go programmin...` | 以英文句号 `.` 结尾 |
| [go-gopkg-inf.v0/go-gopkg-inf.v0.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-gopkg-inf.v0/go-gopkg-inf.v0.spec) | `Package inf (type inf.Dec) implements "infinite-precision...` | 以英文句号 `.` 结尾 |
| [go-gopkg-yaml.v2/go-gopkg-yaml.v2.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-gopkg-yaml.v2/go-gopkg-yaml.v2.spec) | `YAML support for the Go language.` | 以英文句号 `.` 结尾 |
| [go-gopkg-yaml.v3/go-gopkg-yaml.v3.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-gopkg-yaml.v3/go-gopkg-yaml.v3.spec) | `YAML support for the Go language.` | 以英文句号 `.` 结尾 |
| [go-md2man/go-md2man.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-md2man/go-md2man.spec) | `Converts markdown into roff (man pages).` | 以英文句号 `.` 结尾 |
| [go-sourcehut-sbinet-gg/go-sourcehut-sbinet-gg.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-sourcehut-sbinet-gg/go-sourcehut-sbinet-gg.spec) | `gg is a library for rendering 2D graphics in pure Go.` | 以英文句号 `.` 结尾 |
| [go-uber-zap/go-uber-zap.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/go-uber-zap/go-uber-zap.spec) | `Blazing fast, structured, leveled logging in Go.` | 以英文句号 `.` 结尾 |
| [lsscsi/lsscsi.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/lsscsi/lsscsi.spec) | `The lsscsi command lists information about SCSI devices i...` | 以英文句号 `.` 结尾 |
| [minio/minio.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/minio/minio.spec) | `MinIO is a high-performance, S3 compatible object store, ...` | 以英文句号 `.` 结尾 |
| [ollama/ollama.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/ollama/ollama.spec) | `Get up and running with OpenAI gpt-oss, DeepSeek-R1, Gemm...` | 以英文句号 `.` 结尾 |
| [python-blis/python-blis.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/python-blis/python-blis.spec) | `The Blis BLAS-like linear algebra library, as a self-cont...` | 以英文句号 `.` 结尾 |
| [python-blivet/python-blivet.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/python-blivet/python-blivet.spec) | `Blivet is a python module for system storage configuration.` | 以英文句号 `.` 结尾 |
| [python-cart/python-cart.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/python-cart/python-cart.spec) | `Python implementation of the CaRT library for (un)inertin...` | 以英文句号 `.` 结尾 |
| [python-claripy/python-claripy.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/python-claripy/python-claripy.spec) | `An abstraction layer for constraint solvers.` | 以英文句号 `.` 结尾 |
| [python-docopt-ng/python-docopt-ng.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/python-docopt-ng/python-docopt-ng.spec) | `Jazzband-maintained fork of docopt, the humane command li...` | 以英文句号 `.` 结尾 |
| [python-ipython-pygments-lexers/python-ipython-pygments-lexers.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/python-ipython-pygments-lexers/python-ipython-pygments-lexers.spec) | `Defines a variety of Pygments lexers for highlighting IPy...` | 以英文句号 `.` 结尾 |
| [python-iso639/python-iso639.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/python-iso639/python-iso639.spec) | `ISO639-2 support for Python.` | 以英文句号 `.` 结尾 |
| [python-langtable/python-langtable.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/python-langtable/python-langtable.spec) | `guess reasonable defaults for locale, keyboard, territory...` | 以英文句号 `.` 结尾 |
| [python-pexpect/python-pexpect.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/python-pexpect/python-pexpect.spec) | `Pexpect allows easy control of interactive console applic...` | 以英文句号 `.` 结尾 |
| [python-process-tests/python-process-tests.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/python-process-tests/python-process-tests.spec) | `Tools for testing processes.` | 以英文句号 `.` 结尾 |
| [python-pytest-cov/python-pytest-cov.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/python-pytest-cov/python-pytest-cov.spec) | `Pytest plugin for measuring coverage.` | 以英文句号 `.` 结尾 |
| [python-soxr/python-soxr.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/python-soxr/python-soxr.spec) | `High quality, one-dimensional sample-rate conversion libr...` | 以英文句号 `.` 结尾 |
| [python-standard-chunk/python-standard-chunk.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/python-standard-chunk/python-standard-chunk.spec) | `Module to read IFF chunks.` | 以英文句号 `.` 结尾 |
| [python-standard-sunau/python-standard-sunau.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/python-standard-sunau/python-standard-sunau.spec) | `Provide an interface to the Sun AU sound format.` | 以英文句号 `.` 结尾 |
| [python-watchfiles/python-watchfiles.spec](https://github.com/openRuyi-Project/openRuyi/blob/master/SPECS/python-watchfiles/python-watchfiles.spec) | `Simple, modern and high performance file watching and cod...` | 以英文句号 `.` 结尾 |

## 结论

扫描的 5337 个 spec 文件中，113 个的 `Summary` 以英文句号 `.` 结尾，
违反「`Summary` 不得以英文句号 `.` 结尾」的禁止性规定；未发现含 CJK /
全角字符的非英文 `Summary`。建议将违规文件的 `Summary` 结尾句号删除。
