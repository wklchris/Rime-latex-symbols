# 用于 Rime 的 LaTeX 符号输入配置

*author: wklchris@github*

配置 <input-schema>.custom.yaml 文件来在 [RIME 输入法](https://rime.im/) 中使用 LaTeX 数学符号。

支持的符号：

- 常用数学符号，包括几何、微积分。
- 被 LaTeX 主数学宏包 amsmath/amssymb 支持的一些常用符号：
  * 运算符与关系符
  * 箭头符号
- 希腊字母与罗马数字
- 少量其他符号

## 使用方法

此处以 Windows 上的微软双拼 RIME（小狼毫 Weasel）用户为例。

1. 首先，根据你的使用场景，选用你需要复制的文件：

   * (a) 优先场景（覆盖默认的 symbols.yaml 字符配置）：使用 `latexmath.yaml` 文件。
   * (b) 合并场景（将 symbols.yaml 配置合并过来）：使用 `latexmath_compatible.yaml` 文件。

2. 将在上一步中选择的 YAML 文件复制到 RIME 程序文件夹下的 data 目录中：`RIME/weasel-0.xx/data`。

   * 如果你选择了合并场景，请将复制后的 `latexmath_compatible.yaml` 文件重命名为 `latexmath.yaml` 。

   或者，可以将该 YAML 文件复制到同步盘，并用符号链接的形式来指向。这样的好处是可以在多个设备上同步该 yaml 文件的更改。下例以 latexmath.yaml 文件与 Onedrive 同步为例：
   1. 复制文件到 Onedrive 下的 `Sync-Misc\Rime` 文件夹（示例）。该路径可以自定义。
   2. 以管理员身份运行 Powershell，并切换目录到 Rime 程序文件夹下的 `data` 子文件夹（示例）：
      ```
      cd "C:\MyApps\Rime\weasel-0.14.3\data"
      ```
   3. 创建一个指向在上述步骤中复制到 Onedrive 的 YAML 文件的符号链接：
      ```
      New-Item -ItemType SymbolicLink -Path latexmath.yaml -Target "${env:onedrive}\Sync-Misc\Rime\latexmath.yaml"
      ```
      如果使用自定义的 Onedrive 路径，请相应地替换上述命令中的 `\Sync-Misc\Rime` 字符串。

4. 如上在 data 目录中复制好文件后，打开用户文件夹下微软双拼（`double_pinyin_mspy`）的 `custom` 配置文件 `double_pinyin_mspy.custom.yaml`，更新键值：
   ```
   patch:
     punctuator/import_preset: latexmath
     recognizer/patterns:
       punct: "^/([0-9]0?|[A-Za-z]+)$"
   ```
3. 右键点击托盘区的 RIME 图标，点击“重新部署”以应用更改。

## 完整的符号支持列表

支持的符号：

| 输入键位 | 输出符号列表 |
| :--- | :--- |
| /dots | …, ⋯, ⋮, ⋰, ⋱ |
| /cdots | …, ⋯, ⋮, ⋰, ⋱ |
| /ldots | …, ⋯, ⋮, ⋰, ⋱ |
| /vdots | …, ⋯, ⋮, ⋰, ⋱ |
| /ddots | …, ⋯, ⋮, ⋰, ⋱ |
| /forall | ∀ |
| /exists | ∃ |
| /because | ∵ |
| /therefore | ∴ |
| /sum | ∑ |
| /prod | ∏ |
| /sqrt | √, ∛, ∜ |
| /propto | ∝ |
| /ratio | ∶ |
| /inf | ∞ |
| /infty | ∞ |
| /empty | ∅ |
| /log | ㏒ |
| /ln | ㏑ |
| /hslash | ℏ |
| /angle | ∠ |
| /parallel | ∥ |
| /perp | ⊥ |
| /sim | ∼, ≃, ≅ |
| /simeq | ∼, ≃, ≅ |
| /partial | ∂ |
| /nabla | ∇ |
| /int | ∫ |
| /iint | ∬ |
| /iiint | ∭ |
| /oint | ∮ |
| /oiint | ∯ |
| /oiiint | ∰ |
| /plus | +, ⊕ |
| /minus | -, ⊖ |
| /times | ×, ⊗, ·, ⊙, ∘, ∙, ⋆, ∗ |
| /dot | ·, ⊙, ∘, ∙ |
| /cdot | ·, ⊙, ∘, ∙ |
| /star | ⋆, ∗ |
| /ast | ∗ |
| /bullet | ∙ |
| /div | ÷, ⊘ |
| /pm | ±, ∓ |
| /setop | ∪, ∩, ∖, ∨, ∧ |
| /cup | ∪ |
| /cap | ∩ |
| /setminus | ∖ |
| /vee | ∨ |
| /lor | ∨ |
| /wedge | ∧ |
| /land | ∧ |
| /eq | ≡, ≔, ≈, ≌, ≝, ≜, ≟ |
| /approx | ≈ |
| /neq | ≠, ≶, ≷, ⪋, ⪌ |
| /le | <, ≤, ⩽, ≪, ≯ |
| /prec | ≺, ≼ |
| /ge | >, ≥, ⩾, ≫, ≮ |
| /succ | ≻, ≽ |
| /subset | ⊂, ⊆, ⫅, ⫋ |
| /supset | ⊃, ⊇, ⫆, ⫌ |
| /in | ∈ |
| /ni | ∋ |
| /notin | ∉ |
| /implies | ⟹, ⇏, ⇒ |
| /impliedby | ⟸, ⇍, ⇐ |
| /iff | ⟺, ⇔ |
| /left | ←, ⟵, ⇦, 🡨, ↼, ↽, ⮘, ⮜ |
| /leftarrow | ←, ⟵, ⇦, 🡨, ↼, ↽, ⮘, ⮜ |
| /longleft | ⟵ |
| /right | →, ⟶, ⇨, 🡪, ⮚, ⮞ |
| /rightarrow | →, ⟶, ⇨, 🡪, ⮚, ⮞ |
| /longright | ⟶ |
| /leftright | ↔, ⇄, ⇆, ⇌, ⇋, ⇔ |
| /up | ↑, ⇧, 🡩, ⮙, ⮝ |
| /uparrow | ↑, ⇧, 🡩, ⮙, ⮝ |
| /down | ↓, ⇩, 🡫, ⮛, ⮟ |
| /downarrow | ↓, ⇩, 🡫, ⮛, ⮟ |
| /updown | ↕, ⇅, ⇵, ⥮, ⥯, ⇕ |
| /nwarrow | ↖ |
| /nearrow | ↗ |
| /swarrow | ↙ |
| /searrow | ↘ |
| /arrow | ←, →, ↑, ↓, ↖, ↗, ↙, ↘ |
| /greek | α, β, γ, δ, ε, ζ, η, θ |
| | ι, κ, λ, μ, ν, ξ, ο, π |
| | ρ, σ, τ, υ, φ, χ, ψ, ω |
| /greekc | Α, Β, Γ, Δ, Ε, Ζ, Η, Θ |
| | Ι, Κ, Λ, Μ, Ν, Ξ, Ο, Π |
| | Ρ, Σ, Τ, Υ, Φ, Χ, Ψ, Ω |
| /alpha | α, Α |
| /beta | β, Β |
| /gamma | γ, Γ |
| /delta | δ, Δ |
| /epsilon | ε, Ε |
| /zeta | ζ, Ζ |
| /eta | η, Η |
| /theta | θ, Θ |
| /iota | ι, Ι |
| /kappa | κ, Κ |
| /lambda | λ, Λ |
| /mu | μ, Μ |
| /nu | ν, Ν |
| /xi | ξ, Ξ |
| /omicron | ο, Ο |
| /pi | π, Π |
| /rho | ρ, Ρ |
| /sigma | σ, Σ |
| /tau | τ, Τ |
| /upsilon | υ, Υ |
| /phi | φ, Φ |
| /chi | χ, Χ |
| /psi | ψ, Ψ |
| /omega | ω, Ω |
| /roman | ⅰ, ⅱ, ⅲ, ⅳ, ⅴ, ⅵ, ⅶ, ⅷ |
| | ⅸ, ⅹ, ⅺ, ⅻ, ⅼ, ⅽ, ⅾ, ⅿ |
| /romanc | Ⅰ, Ⅱ, Ⅲ, Ⅳ, Ⅴ, Ⅵ, Ⅶ, Ⅷ |
| | Ⅸ, Ⅹ, Ⅺ, Ⅻ, Ⅼ, Ⅽ, Ⅾ, Ⅿ |
| /gender | ♂, ♀, ⚢, ⚣, ⚤, ⚥, ⚦ |

## 贡献与许可证

本配置的部分内容来自官方 Weasel 项目部署后的默认 `data/symbols.yaml` 文件。

许可证：[GPLv3](./LICENSE)
